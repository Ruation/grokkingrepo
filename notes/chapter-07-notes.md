# Dijkstra's Algorithm

Dijkstra's algorithm is used to find the **shortest path in a weighted graph**.

It calculates the minimum cost from a **starting node** to all other nodes in the graph.

⚠️ The algorithm only works with **non-negative edge weights**.

---

## Key Idea

The algorithm always selects the **unprocessed node with the lowest cost** and updates the cost of reaching its neighbors.

By repeating this process, it gradually builds the shortest path through the graph.

---

## How the Algorithm Works

1. Assign a cost to every node.
   - Start node → cost **0**
   - All other nodes → **infinity**

2. Create a table to store the **parent node** of each node.

3. While there are still unprocessed nodes:
   - Select the **lowest-cost unprocessed node**
   - Update the cost of its neighbors if a cheaper path is found
   - Mark the node as **processed**

4. Continue until all nodes are processed.

---

## Example

Graph:

Start → A (6)  
Start → B (2)  
B → A (3)  
B → End (5)  
A → End (1)

Shortest path:

Start → B → A → End

Total cost:

2 + 3 + 1 = 6

➡️ [View Dijktra's algorithm implementation ](../code/dijkstra.py)

---

## Time Complexity

Basic implementation:

O(V²)

Optimized with a priority queue (heap):

O((V + E) log V)

Where:

- **V** = number of vertices (nodes)
- **E** = number of edges

---

## Data Structures Used

Dijkstra's algorithm typically uses:

- Graph (adjacency list)
- Cost table
- Parent table
- Processed set

---

## Limitations

Dijkstra's algorithm **does not work with negative edge weights**.

If a graph contains negative weights, another algorithm such as **Bellman–Ford** must be used.

---

## Summary

- Finds the **shortest path in a weighted graph**
- Works only with **non-negative weights**
- Always processes the **lowest-cost node first**
- Updates neighbor costs until the optimal path is found
