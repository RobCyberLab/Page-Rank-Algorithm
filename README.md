# 📉Page Rank Algorithm📈

In this project, we will analyze the execution of the PageRank algorithm.

Note: Due to privacy policies, I am not allowed to post the dataset publicly.

---

## Table of Contents 📑

1. [Requirements](#requirements)
2. [Implementation Notes](#implementation-notes)
3. [Mathematical Background](#mathematical-background)

---

## Requirements📋

1. Each student will draw (on a sheet of paper) a **directed graph** with n = 10 nodes and random arcs.
2. The graph will be represented using Python data structures (any representation can be used).
3. Based on the graph, construct the transition matrix M.
4. The vector v₀ will be initialized as:
   ```
   v₀ = [1/n]
        [1/n]
        [...]
        [1/n]
   ```
   and will be updated through repeated multiplications with the transition matrix M.
5. The algorithm stops when the ranks vector changes sufficiently little between two generations (`|v' - v| < ε`).
6. Graphically represent using a bar chart the color rankings of n nodes at each step.

---

## Implementation Notes📝

- The program should use Python's built-in data structures.
- The transition matrix M represents the probability of transitioning from one node to another.
- The initial vector v₀ assigns equal probability to all nodes.
- The convergence criterion ε determines when the algorithm stops.
- The visualization should show how node rankings evolve over iterations.

---

## Mathematical Background📚

The PageRank algorithm uses an iterative approach where:
- M is the transition matrix.
- v is the ranking vector.
- The process continues until convergence.
- Final values represent the relative importance of each node in the graph.

---
