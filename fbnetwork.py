import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Load the Facebook social network dataset
G = nx.read_edgelist('facebook_combined.txt', nodetype=int)

def random_walk(graph, start_node, num_steps):
    """
    Perform a random walk on a network starting from a given node.

    Parameters:
    graph (networkx.Graph): The input network.
    start_node (int): The index of the node to start the random walk from.
    num_steps (int): The number of steps to take in the random walk.

    Returns:
    list: The indices of the nodes traversed in the random walk.
    """
    nodes = list(graph.nodes())
    curr_node = start_node
    visited = [curr_node]
    for i in range(num_steps):
        neighbors = list(graph.neighbors(curr_node))
        if len(neighbors) == 0:
            break
        probs = [graph[curr_node][n]['weight'] for n in neighbors]
        probs /= np.sum(probs)
        curr_node = np.random.choice(neighbors, p=probs)
        visited.append(curr_node)
        print('Step {}: Node {}'.format(i+1, curr_node))
    return visited

# Perform a random walk starting from node 0
num_steps = 20
walk = random_walk(G, start_node=0, num_steps=num_steps)

# Plot the graph
pos = nx.spring_layout(G, k=0.1, iterations=50)
fig, ax = plt.subplots()

# Function to update the plot at each animation frame
def update(num):
    ax.clear()
    nx.draw_networkx_nodes(G, pos, node_size=5, node_color='gray', alpha=0.3)
    nx.draw_networkx_nodes(G, pos, nodelist=walk[:num], node_size=10, node_color='r')
    ax.set_title(f"Step {num}: Node {walk[num]}")

# Create the animation object
ani = FuncAnimation(fig, update, frames=num_steps+1, interval=1000, repeat=False)

# Save the animation as a gif file
ani.save('facebook_random_walk.gif', writer='imagemagick')
