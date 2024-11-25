import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

plt.figure(figsize=(10, 10))
ax = plt.gca()
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.set_aspect('equal')

obstacles = [
    [(-0.218391, 0.225865), (-0.74632, -0.078935), (-0.44152, -0.606865), (0.086409, -0.302065)],
    [(0.44152, 0.606865), (-0.086409, 0.302065), (0.218391, -0.225865), (0.74632, 0.078935)],
    [(-0.6952, 1.3048), (-1.3048, 1.3048), (-1.3048, 0.6952), (-0.6952, 0.6952)],
    [(1.3048, -0.6952), (0.6952, -0.6952), (0.6952, -1.3048), (1.3048, -1.3048)],
    [(0.873302, 1.435526), (0.284474, 1.593302), (0.126698, 1.004474), (0.715526, 0.846698)],
    [(-0.568948, -1), (-1, -0.568948), (-1.43105, -1), (-1, -1.43105)]
]

initial_pos = (-1.5, -2)
initial_pos_red = (-2, 0)

target_positions = [
    (-0.86717, -0.35655),
    (-0.27732, 0.55024),
    (0.28612, -0.49741),
    (-1.01683, 1.52745),
    (0.67349, 0.62947),
    (-1.37779, -1.36899),
    (1.54506, -0.99923)
]

x_coords = [-1.5, 2, 0, -1.4, -2, -2, -0.8, -2, -2, -1, -0.3, -0.3,-0.1, -0.1, -0.1, 1.2, 1.2, 0.7, 0.7,
             1.2, 1, 0.3, 1.5, 1.5, 1.5]
y_coords = [-2, -1.5, -2, -1.4, -1, -0.4, -0.4, 1, 1.5, 1.5, 1.5, 0.5,0.5, 0.5, 2, 2, 0.5, 0.7, 0.6,
             0.3, 0, -0.5, -0.5, -1, -1.5]

x_coords_red = [-2, -1.4, -2, -2, -0.8, -2, -2, -1, -0.3, -0.3,-0.1, -0.1, -0.1, 1.2, 1.2, 0.7, 0.7,
             1.2, 1, 0.3, 1.5, 1.5, 2.0]
y_coords_red = [0, -1.4, -1, -0.4, -0.4, 1, 1.5, 1.5, 1.5, 0.5,0.5, 0.5, 2, 2, 0.5, 0.7, 0.6,
             0.3, 0, -0.5, -0.5, -1, -1]




for obstacle in obstacles:
    polygon = Polygon(obstacle, facecolor='gray', alpha=0.3)
    ax.add_patch(polygon)

target_x = [p[0] for p in target_positions]
target_y = [p[1] for p in target_positions]
ax.scatter(target_x, target_y, color='green', s=50, label='Targets')

plt.plot(x_coords, y_coords, 'b-', linewidth=2, label='Robot Path')
plt.scatter(x_coords, y_coords, color='blue', s=30)  # Show the waypoints

plt.plot(x_coords_red, y_coords_red, 'r-', linewidth=2, label='Robot Path')
plt.scatter(x_coords_red, y_coords_red, color='red', s=30)  # Show the waypoints

plt.scatter(initial_pos_red[0], initial_pos_red[1], color='red', s=100, marker='*', label='Initial Position')

plt.scatter(initial_pos[0], initial_pos[1], color='blue', s=100, marker='*', label='Initial Position')

plt.grid(True)
plt.legend()

for i, (x, y) in enumerate(zip(x_coords, y_coords)):
    ax.annotate(str(i), (x, y), xytext=(5, 5), textcoords='offset points', fontsize=8)

plt.savefig('robot_new_path.png')
plt.close()