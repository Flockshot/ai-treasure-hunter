#Muhammad Somaan 2528404
#Muhammad Hashir Faraz 2528545

# Class to represent the map as a tree graph.
class MyTree:
    # Inner Class to represent the edges of the tree graph.
    class Edge:
        def __init__(self, node_from, node_to, cost):
            self.node_from = node_from
            self.node_to = node_to
            self.cost = cost

        def __str__(self):
            return self.node_to.name + " " + str(self.cost)

    # Constructor for the tree graph, which takes the name of the node, and the heuristic value.
    def __init__(self, name: str, heuristic: int):
        self.name = name
        self.heuristic = heuristic
        # List of edges to other nodes.
        self.paths: list[MyTree.Edge] = list()

    # Method to add an edge to the tree graph, which takes the node to connect to, and the cost of the edge.
    def add_edge(self, node_to, cost: int):
        self.paths.append(MyTree.Edge(self, node_to, cost))

    def __str__(self):
        return self.name


# Class to represent the path taken to get to a node.
class Path:
    # List of nodes in the path.
    journey: list[MyTree] = list()

    # Constructor for the path, which takes the starting node, and the total cost of the path.
    def __init__(self, start_node: MyTree, total_cost: int):
        self.start_node = start_node
        self.current_node = start_node
        self.total_cost = total_cost

    # Method to add a path to the path, which takes the edge to add to the path,
    # and adds the cost of the edge to the total cost.
    def add_path(self, path_to: MyTree.Edge):
        self.current_node = path_to.node_to
        self.journey.append(self.current_node)
        self.total_cost += path_to.cost

    # Method to copy a path, which takes the path to copy, and returns a copy of the path.
    @classmethod
    def copy(cls, copy_from):
        path_copy = cls(copy_from.start_node, copy_from.total_cost)
        path_copy.current_node = copy_from.current_node
        path_copy.journey = copy_from.journey.copy()
        return path_copy

    # Method to print the path.
    def __str__(self):
        journey_str = self.start_node.name
        for node in self.journey:
            journey_str += " -> " + node.name
        return str(journey_str) + ", Total Cost: " + str(self.total_cost)


# Method to run the maze, which takes the name of the maze file.
def run_maze(maze_file_name: str):

    print("\nRunning maze: " + maze_file_name)

    maze_file = open(maze_file_name, "r")

    # Variables to store the size of the maze, the start and end nodes, and the costs of the nodes.
    size_x = 0
    size_y = 0
    start_node_x = 0
    start_node_y = 0
    end_node_x = 0
    end_node_y = 0
    nodes_text = list()

    # Read the maze file.
    for line in maze_file.readlines():

        # If the line is the size of the maze, split the line by the equals sign, and then split the result by the
        # comma. to get the size of the maze.
        if line.lower().startswith("size"):
            file_info = line.split("=")[1].split(",")
            size_x = int(file_info[0])
            size_y = int(file_info[1])
        # If the line is the start node, split the line by the equals sign, and then split the result by the
        # comma. to get the start node's x and y coordinates.
        elif line.lower().startswith("start"):
            file_info = line.split("=")[1].split(",")
            start_node_x = int(file_info[0])
            start_node_y = int(file_info[1])
        # If the line is the end node, split the line by the equals sign, and then split the result by the
        # comma. to get the end node's x and y coordinates.
        elif line.lower().startswith("end"):
            file_info = line.split("=")[1].split(",")
            end_node_x = int(file_info[0])
            end_node_y = int(file_info[1])
        # If the line is a comment, ignore it.
        elif line.lower().startswith("#"):
            next
        # If the line is a node, split the line by the comma, and add the node to the list of nodes.
        else:
            stripped_line = line.strip().split(",")
            # Inserting the node at the index of the node, so that the index of the node in the list is the same as
            # the index of the node in the maze.
            nodes_text.insert(int(stripped_line[0]), stripped_line)

    # Close the maze file.
    maze_file.close()

    # Method to convert the x and y coordinates of a node to an index in list.
    def x_y_to_index(x: int, y: int, max_y: int):
        return x * max_y + y

    # Method to calculate the manhattan distance between two nodes.
    def calc_manhattan_distance(index, end_x, end_y, size_y):
        x = index // size_y
        y = index % size_y
        return abs(end_x - x) + abs(end_y - y)

    # List to store the nodes in the maze.
    maze_nodes = list()

    # Create the nodes in the maze.
    for i in range(len(nodes_text)):
        maze_nodes.append(MyTree(nodes_text[i][0], calc_manhattan_distance(i, end_node_x, end_node_y, size_y)))

    # Add the edges to the nodes in the maze.
    for i in range(len(nodes_text)):
        # Go through the paths of a node, such as up, down, right, and left.
        for j in range(1, len(nodes_text[i])):
            # If the path is possible to take, such as a node can go up, add the edge to the node.
            if nodes_text[i][j] == "true":
                # If the path is up, add the edge to the node above the current node.
                if j == 1:
                    maze_nodes[i].add_edge(maze_nodes[i - 1], 1)
                # If the path is down, add the edge to the node to the right of the current node.
                elif j == 2:
                    maze_nodes[i].add_edge(maze_nodes[i + 1], 1)
                # If the path is right, add the edge to the node below the current node.
                elif j == 3:
                    maze_nodes[i].add_edge(maze_nodes[i + size_y], 1)
                # If the path is left, add the edge to the node to the left of the current node.
                elif j == 4:
                    maze_nodes[i].add_edge(maze_nodes[i - size_y], 1)

    # Select the start and end nodes from the list of nodes, by the given x and y coordinates in the maze file.
    start = maze_nodes[x_y_to_index(start_node_x, start_node_y, size_y)]
    goal = maze_nodes[x_y_to_index(end_node_x, end_node_y, size_y)].name
    print("Goal Node: " + goal)

    queue: list[Path] = [Path(start, 0)]
    # keep track of visited nodes to prevent infinite loops
    visited: list[MyTree] = list()

    print("\nApplying UCS")
    # apply UCS algorithm to start variable
    while True:
        # sort queue by total cost
        queue.sort(key=lambda path: path.total_cost)
        to_pop = queue[0]
        # add the popped node to the visited list
        visited.append(to_pop.current_node)

        print(to_pop)

        # if the popped node is the goal, print the solution path and break
        if to_pop.current_node.name == goal:
            print("Solution Path: ", to_pop)
            break

        # add all the edges of the popped node to the queue
        for edge in to_pop.current_node.paths:
            # if the node is already visited, skip it
            if visited.__contains__(edge.node_to):
                continue
            new_path = Path.copy(to_pop)
            new_path.add_path(edge)
            queue.append(new_path)

        queue.pop(0)

    # apply A* algorithm to start variable
    queue: list[Path] = [Path(start, 0)]
    solutions: list[Path] = list()
    # keep track of visited nodes to prevent infinite loops
    visited: list[MyTree] = list()

    print("\nApplying A*")
    # apply A* algorithm while there are still nodes to visit
    while len(queue) > 0:
        # sort queue by total cost + heuristic
        queue.sort(key=lambda path: path.total_cost + path.current_node.heuristic)
        to_pop = queue[0]

        print(to_pop)

        # if the popped node is the goal, add it to the solutions list
        if to_pop.current_node.name == goal:
            solutions.append(to_pop)
            queue.pop(0)
            continue

        # add the popped node to the visited list
        visited.append(to_pop.current_node)

        # add all the edges of the popped node to the queue
        for edge in to_pop.current_node.paths:
            # if the node is already visited, skip it
            if visited.__contains__(edge.node_to):
                continue
            new_path = Path.copy(to_pop)
            new_path.add_path(edge)
            # if the new path is not the same as the popped node, add it to the queue
            if new_path.current_node.name != to_pop.current_node.name:
                queue.append(new_path)

        queue.pop(0)
    print("All Solutions found: ")
    for solution in solutions:
        print(solution)
    # sort the solutions list by total cost
    solutions.sort(key=lambda path: path.total_cost)
    print("Best Solution: ", solutions[0])

    # apply BFS
    queue: list[Path] = [Path(start, 0)]
    # keep track of visited nodes to prevent infinite loops
    visited: list[MyTree] = list()

    print("\nApplying BFS")
    # apply BFS algorithm while there are still nodes to visit
    while True:
        to_pop = queue[0]
        # add the popped node to the visited list
        visited.append(to_pop.current_node)

        print(to_pop)

        # if the popped node is the goal, print the solution path and break
        if to_pop.current_node.name == goal:
            print("Solution Path: ", to_pop)
            break

        # add all the edges of the popped node to the queue
        for edge in to_pop.current_node.paths:
            # if the node is already visited, skip it
            if visited.__contains__(edge.node_to):
                continue
            new_path = Path.copy(to_pop)
            new_path.add_path(edge)
            if new_path.current_node.name != to_pop.current_node.name:
                queue.append(new_path)

        queue.pop(0)


# Method to run the maze, 1st example case (same as the one given in the assignment)
run_maze("maze.txt")
# Method to run the maze, 2nd example case
run_maze("maze2.txt")
