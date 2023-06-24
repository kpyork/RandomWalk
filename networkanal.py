import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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
    return visited

def update(num, data, ax):
    """
    Update function for the animation.

    Parameters:
    num (int): The frame number.
    data (dict): A dictionary containing the network and the sequence of nodes visited so far.
    ax (matplotlib.axes.Axes): The axes to draw the network on.

    Returns:
    list: A list of the artists created by the update function.
    """
    ax.clear()
    nx.draw_networkx_nodes(data['graph'], data['pos'], nodelist=data['node_seq'][:num], node_color='r')
    nx.draw_networkx_nodes(data['graph'], data['pos'], nodelist=[data['node_seq'][0]], node_color='g')
    nx.draw_networkx_edges(data['graph'], data['pos'], alpha=0.5)
    ax.axis('off')
    ax.set_title('Step {}'.format(num))
    return []

def plot_walk_animation(graph, node_seq):
    """
    Plot an animation of the nodes traversed in a random walk on a network.

    Parameters:
    graph (networkx.Graph): The input network.
    node_seq (list): The indices of the nodes traversed in the random walk.
    """
    fig, ax = plt.subplots(figsize=(6, 4))
    pos = nx.spring_layout(graph)
    data = {'graph': graph, 'pos': pos, 'node_seq': node_seq}
    anim = FuncAnimation(fig, update, frames=len(node_seq), fargs=(data, ax), repeat=False)
    anim.save('random_walk.gif', writer='pillow', fps=5)
    plt.show()

# Example usage
G = nx.karate_club_graph()
walk = random_walk(G, start_node=0, num_steps=100)
plot_walk_animation(G, walk)
