# Dynamic Programming

Dynamic programming is an algorithmic technique used to solve complex problems by **breaking them into smaller overlapping subproblems**.

Instead of solving the same subproblem many times, dynamic programming **stores the results** and reuses them later. This greatly improves efficiency.

Dynamic programming is often used for **optimization problems**, where we want to find the best solution among many possibilities.

---

## Key Idea

Dynamic programming works by:

1. Breaking a problem into **smaller subproblems**
2. Solving each subproblem **once**
3. **Storing the result** for future use

This avoids repeated work and reduces the overall time complexity.

---

## Two Main Approaches

### 1. Memoization (Top-Down)

The algorithm uses **recursion** and stores previously computed results.

When a subproblem appears again, the stored result is returned instead of recalculating it.

Example structure:

if solution already computed:
return stored result

else:
compute solution
store result


---

### 2. Tabulation (Bottom-Up)

The problem is solved **iteratively**, starting from the smallest subproblems and building up to the final solution.

Results are stored in a **table** (usually an array or matrix).

---

## Characteristics of Dynamic Programming Problems

Dynamic programming works best when a problem has:

- **Overlapping subproblems**  
  The same smaller problems appear many times.

- **Optimal substructure**  
  The optimal solution can be built from optimal solutions to smaller subproblems.

---

## Example Problems

Common problems solved with dynamic programming include:

- Fibonacci sequence
- Longest common subsequence
- Knapsack problem
- Shortest path algorithms
- Edit distance

---

## Advantages

- Avoids repeated calculations
- Much faster than naive recursive solutions
- Works well for many optimization problems

---

## Limitations

Dynamic programming solutions can require:

- More **memory**
- Careful problem analysis to identify subproblems

---

## Summary

Dynamic programming:

- is useful when you're trying to optimize something given a **constraint**
- Breaks problems into **overlapping subproblems**
- Stores solutions to **avoid repeated work**
- Uses **memoization** or **tabulation**
- Is commonly used for **optimization problems**
