import networkx as nx #library for network analysis
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def random_walk(graph, start_node, num_steps):
    nodes = list(graph.nodes())
    curr_node = start_node
    visited = [curr_node]
    for i in range(num_steps):
        neighbors = list(graph.neighbors(curr_node))
        if len(neighbors) == 0:
            break
        probs = [graph[curr_node][n]['weight'] for n in neighbors] #
        probs /= np.sum(probs) #so that the sum of the probabilities of the neighbors is 1
        curr_node = np.random.choice(neighbors, p=probs)
        visited.append(curr_node)
        print('Step {}: Node {}'.format(i+1, curr_node))
    return visited

# Example usage
G = nx.karate_club_graph()
num_steps = 100
walk = random_walk(G, start_node=0, num_steps=num_steps)

# Plotting the graph
pos = nx.spring_layout(G)
fig, ax = plt.subplots()

# Function to update the plot at each animation frame
def update(num):
    ax.clear()
    nx.draw(G, pos, ax=ax, node_color='gray', node_size=200)
    nx.draw_networkx_nodes(G, pos, nodelist=walk[:num], node_color='r', node_size=200)
    ax.set_title(f"Step {num}: Node {walk[num]}")
    
# Creating the animation object
ani = FuncAnimation(fig, update, frames=num_steps+1, interval=100, repeat=False)

# Saving the animation as a gif file
ani.save('random_walk.gif', writer='imagemagick')