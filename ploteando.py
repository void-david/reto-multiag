import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Setup the plot
plt.figure(figsize=(10, 10))
ax = plt.gca()
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.set_aspect('equal')

# Define obstacles
obstacles = [
    [(-0.218391, 0.225865), (-0.74632, -0.078935), (-0.44152, -0.606865), (0.086409, -0.302065)],
    [(0.44152, 0.606865), (-0.086409, 0.302065), (0.218391, -0.225865), (0.74632, 0.078935)],
    [(-0.6952, 1.3048), (-1.3048, 1.3048), (-1.3048, 0.6952), (-0.6952, 0.6952)],
    [(1.3048, -0.6952), (0.6952, -0.6952), (0.6952, -1.3048), (1.3048, -1.3048)],
    [(0.873302, 1.435526), (0.284474, 1.593302), (0.126698, 1.004474), (0.715526, 0.846698)],
    [(-0.568948, -1), (-1, -0.568948), (-1.43105, -1), (-1, -1.43105)]
]

# Initial positions for robots
initial_positions = [(-1.5, -2), (-2, 0)]

# Target positions
target_positions = [
    (-0.86717, -0.35655),
    (-0.27732, 0.55024),
    (0.28612, -0.49741),
    (-1.01683, 1.52745),
    (0.67349, 0.62947),
    (-1.37779, -1.36899),
    (1.54506, -0.99923)
]

# Plot obstacles
for obstacle in obstacles:
    polygon = Polygon(obstacle, facecolor='gray', alpha=0.3)
    ax.add_patch(polygon)

# Plot initial positions
ax.scatter(initial_positions[0][0], initial_positions[0][1], color='blue', s=100, label='Robot 1 Start')
ax.scatter(initial_positions[1][0], initial_positions[1][1], color='red', s=100, label='Robot 2 Start')

# Plot target positions
target_x = [p[0] for p in target_positions]
target_y = [p[1] for p in target_positions]
ax.scatter(target_x, target_y, color='green', s=50, label='Targets')

# Add grid and legend
plt.grid(True)
plt.legend()

# Save the plot to a file
plt.savefig('robot_environment.png')
plt.close()