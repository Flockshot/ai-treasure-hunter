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


treasure = MyTree("Treasure", 0)

desert = MyTree("Desert", 3)
desert.add_edge(treasure, 10)

forest = MyTree("Forest", 2)
forest.add_edge(treasure, 4)

stormy_ocean = MyTree("Stormy Ocean", 2)
stormy_ocean.add_edge(desert, 4)
stormy_ocean.add_edge(stormy_ocean, 20)

start = MyTree("Start", 1)
start.add_edge(stormy_ocean, 4)
start.add_edge(forest, 7)

# queue for the nodes to be visited
queue: list[Path] = [Path(start, 0)]
goal = "Treasure"

print("Applying UCS")
# Applying UCS
while True:
    # sort the queue by the total cost of the path
    queue.sort(key=lambda path: path.total_cost)
    to_pop = queue[0]

    # print the path
    print(to_pop)

    # if the current node is the goal, print the path and break
    if to_pop.current_node.name == goal:
        print("Solution Path: ", to_pop)
        break

    # add the edges paths to the queue
    for edge in to_pop.current_node.paths:
        new_path = Path.copy(to_pop)
        new_path.add_path(edge)
        queue.append(new_path)

    queue.pop(0)

# apply A* algorithm to start variable
queue: list[Path] = [Path(start, 0)]
goal = "Treasure"
# list of solutions
solutions: list[Path] = list()

print("\nApplying A*")
# Applying A* while there are still nodes to visit
while len(queue) > 0:
    # sort the queue by the total cost of the path + the heuristic value of the node
    queue.sort(key=lambda path: path.total_cost + path.current_node.heuristic)
    to_pop = queue[0]

    print(to_pop)

    # if the current node is the goal, add the path to the solutions list
    if to_pop.current_node.name == goal:
        solutions.append(to_pop)

    # add the edges paths to the queue
    for edge in to_pop.current_node.paths:
        new_path = Path.copy(to_pop)
        new_path.add_path(edge)
        # if the node is not already in the path, add the path to the queue, to prevent loops
        if new_path.current_node.name != to_pop.current_node.name:
            queue.append(new_path)

    queue.pop(0)
# sort the solutions by the total cost of the path
solutions.sort(key=lambda path: path.total_cost)
# print the best solution with the lowest cost
print("Best Solution: ", solutions[0])
