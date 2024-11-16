import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# 1. Generate a directed graph using gn_graph
n = 10
G = nx.gn_graph(n, seed=42)

# 2. Create adjacency list representation
adj_list = {i: list(G.successors(i)) for i in G.nodes()}

# 3. Build transition matrix M with specific handling for zero out-degree nodes
M = np.zeros((n, n))
for i in range(n):
    successors = adj_list[i]
    if len(successors) > 0:
        # If node has outgoing edges, distribute probability equally
        for j in successors:
            M[j][i] = 1.0 / len(successors)
    else:
        # If node has no outgoing edges, set probability to 0.015 for all nodes
        M[:, i] = 0.015

# 4. Initialize v0 with equal probabilities
v0 = np.ones(n) / n  # This will give us [0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1]


def pagerank(M, v0, max_iterations=5):
    v = v0
    rankings_history = [v.copy()]

    for _ in range(max_iterations):
        v_next = M @ v
        rankings_history.append(v_next.copy())
        v = v_next

    return rankings_history


# 5. Run PageRank algorithm and collect history
rankings_history = pagerank(M, v0)

# 6. First visualize the graph structure
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos,
        with_labels=True,
        node_color='green',
        edge_color='green',
        node_size=500,
        arrowsize=20,
        arrows=True,
        font_size=12,
        font_weight='bold')
plt.title("Directed Graph Structure")
plt.show()

# Print adjacency list
print("\nAdjacency List:")
for node, neighbors in sorted(adj_list.items()):
    print(f"Node {node}: {neighbors}")

# Print transition matrix
print("\nTransition Matrix M:")
print(M)

# Print initial vector and iterations
print("\nInitial vector v0:")
print(v0)

for idx, rankings in enumerate(rankings_history[1:], 1):
    print(f"\nIteration {idx}:", end=" ")
    np.set_printoptions(precision=8, suppress=True)
    print(rankings)


# 7. Visualize PageRank iterations
def plot_rankings(rankings_history):
    nodes = range(n)

    # First plot iteration 0 (initial state)
    plt.figure(figsize=(10, 6))
    bars = plt.bar(nodes, rankings_history[0], color='green', edgecolor='green')
    plt.title('PageRank Values - Initial State (Iteration 0)')
    plt.xlabel('Node ID')
    plt.ylabel('PageRank Value')
    plt.grid(True, alpha=0.3)

    # Add value labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2., height,
                 f'{height:.3f}',
                 ha='center', va='bottom')

    plt.ylim(0, 0.15)  # Set fixed y-limit for initial state
    plt.xticks(nodes)
    plt.show()

    # Then plot iterations 1-5
    for idx, rankings in enumerate(rankings_history[1:], 1):
        plt.figure(figsize=(10, 6))
        bars = plt.bar(nodes, rankings, color='green', edgecolor='green')
        plt.title(f'PageRank Values - Iteration {idx}')
        plt.xlabel('Node ID')
        plt.ylabel('PageRank Value')
        plt.grid(True, alpha=0.3)

        # Add value labels on top of each bar
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2., height,
                     f'{height:.3f}',
                     ha='center', va='bottom')

        # Set y-axis limit slightly higher than max value for label visibility
        plt.ylim(0, max(rankings) * 1.1)

        # Add xticks for each node
        plt.xticks(nodes)

        plt.show()


# Plot the rankings (bar charts)
print("\nBar charts for PageRank values of all nodes:")
plot_rankings(rankings_history)