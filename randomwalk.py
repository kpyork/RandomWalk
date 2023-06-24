import random
import matplotlib.pyplot as plt

# Set up parameters
n_steps = 1000
start_pos = 0
pos = start_pos
positions = [pos]

# Simulate the random walk
for i in range(n_steps):
    # Randomly choose a direction to move
    if random.random() < 0.5:
        pos -= 1
    else:
        pos += 1
    # Record the new position
    positions.append(pos)

# Plot the results
plt.plot(positions)
plt.xlabel('Time')
plt.ylabel('Position')
plt.title('Random Walk Simulation')
plt.show()
