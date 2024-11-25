import mesa

InitialPositions = open("InitialPositions.txt", "r")
Obstacle_1 = open("Obstacle_1.txt", "r")
Obstacle_2 = open("Obstacle_2.txt", "r")
Obstacle_3 = open("Obstacle_3.txt", "r")
Obstacle_4 = open("Obstacle_4.txt", "r")
Obstacle_5 = open("Obstacle_5.txt", "r")
Obstacle_6 = open("Obstacle_6.txt", "r")
TargetPositions = open("TargetPositions.txt", "r")



Obstacles = [Obstacle_1, Obstacle_2, Obstacle_3, Obstacle_4, Obstacle_5, Obstacle_6]
RectangleObstacles = []


for obstacle in Obstacles:    
    s = obstacle.read().split(sep="\n")
    x = list(map(float, s[0].split(sep=",")))
    y = list(map(float, s[1].split(sep=",")))
    RectangleObstacles.append([x, y])


for rectangle in RectangleObstacles:
    print(rectangle)
