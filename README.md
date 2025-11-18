# AI Treasure Hunter: Pathfinding Algorithm Implementation

![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg?logo=python&logoColor=white)

Designed and implemented a Python-based AI system to explore and compare pathfinding algorithms—specifically Breadth-First Search (BFS), Uniform Cost Search (UCS), and A\* Search—by solving two distinct problems: treasure hunting on a map and maze navigation.

The core of the project involves implementing these algorithms from scratch and applying them to:
* **Task 1 (Treasure Map):** A simple, weighted graph representing a treasure map.
* **Task 2 (Mayan Maze):** A complex, grid-based maze parsed from a text file.

The implementation visualizes the node expansion sequence for each algorithm, providing a clear comparison of efficiency between uninformed (BFS) and informed (UCS, A\*) search strategies.

### 🗺️ Task 1: The Treasure Map

In this task, a simple, weighted graph is used to represent a treasure map. The goal is to find the least-cost path from the "Start" to the "Treasure".

* **Algorithms:** Uniform Cost Search (UCS) and A\* Search.
* **Heuristics:** The A\* algorithm uses a pre-defined heuristic provided in the project specification.
* **Source Code:** `task_1.py`

> **[Image: Screenshot of the Treasure Map graph from ai-treasure-hunter.pdf, Page 2]**
>
> *(**Developer Note:** Place the screenshot of the simple map graph here .)*

### 🏛️ Task 2: The Mayan Maze

This task implements pathfinding in a grid-based maze. The maze layout, including walls, start point, and end point, is parsed from a `.txt` file.

* **Algorithms:** Breadth-First Search (BFS), Uniform Cost Search (UCS), and A\* Search.
* **Heuristics:** The A\* algorithm uses the **Manhattan distance** as its heuristic, calculated dynamically for each node.
* **Source Code:** `task_2.py`

> **[Image: Screenshot of the Maze Grid from ai-treasure-hunter.pdf, Page 4]**
>
> *(**Developer Note:** Place the screenshot of the numbered maze grid here .)*

### ✨ Maze Solution Path (A\* Search)

This image shows the final, optimal path found by the A\* algorithm for the primary maze (`maze.txt`).

> **[Image: Screenshot of the Maze Grid WITH the final path drawn on it]**
>
> *(**Developer Note:** This is your most important visual! Run `task_2.py`, get the "Best Solution" path for `maze.txt`, and draw that path on the maze screenshot.)*

---

## 🤖 Algorithms Implemented

This project builds three fundamental search algorithms from the ground up, managed by a custom `Path` class that tracks the journey and total cost.

1.  **Breadth-First Search (BFS):** An uninformed algorithm that explores all neighbors at the present depth before moving on. It uses a standard FIFO (First-In, First-Out) queue. Guaranteed to find the *shortest* path in terms of number of steps.
2.  **Uniform Cost Search (UCS):** An uninformed algorithm that explores by the lowest cumulative cost. It uses a priority queue (implemented via `list.sort()`), always expanding the path with the smallest `total_cost`. Guaranteed to find the *cheapest* path.
3.  **A\* Search:** An informed, heuristic-based algorithm. It uses a priority queue, sorting paths by the sum of their current cost and a heuristic estimate to the goal (`total_cost + heuristic`). It is both complete and optimal (given an admissible heuristic).

---

## ⚙️ How It Works

### Maze File Format

The `task_2.py` script can parse any maze that follows the format defined in `maze.txt` and `maze2.txt`.

* `size=x,y`: Defines the dimensions of the maze grid.
* `start=x,y`: Sets the (x, y) coordinate for the starting node.
* `end=x,y`: Sets the (x, y) coordinate for the goal node.
* `# ...`: Lines starting with `#` are ignored as comments.
* `node_index,up,down,right,left`: A boolean list that defines the passable walls for each node.

### Core Code Structure

* **`MyTree` Class:** Represents the map as a graph, where each instance is a node that holds its name, heuristic, and a list of edges to its neighbors.
* **`Path` Class:** A data structure that stores the state of a search path, including the full journey (list of nodes) and the `total_cost`.
* **`run_maze(file_name)`:** The main function in `task_2.py`. It:
    1.  Opens and parses the specified maze file.
    2.  Creates a list of `MyTree` nodes, calculating the Manhattan distance heuristic for each one.
    3.  Connects the nodes by adding edges based on the file's boolean values (up, down, left, right).
    4.  Runs BFS, UCS, and A\* search on the constructed graph, printing the results for each.

---

## 🚀 How to Run

### Requirements
* Python 3.11

### Running the Project

This program is designed to be run from a console or an IDE.

1.  Clone the repository.
2.  Open your terminal or command prompt.
3.  Navigate to the project directory.
4.  Run the `task_2.py` file (which contains the maze logic) using Python 3.11.

```bash
python task_2.py
```
> **Note:** The script runs very quickly and will print all outputs to the console before exiting. To see the full output, it is recommended to run the file in an IDE like **PyCharm** or **IDLE**.

### Example Output

The script will print the step-by-step expansion of each algorithm, followed by the solution. The output format for a solution looks like this:

```
Applying A*
...
Best Solution:  0 -> 1 -> 2 -> 10 -> 18 -> 19 -> 20 -> 28 -> 36 -> 44 -> 45 -> 53 -> 61, Total Cost: 14
```