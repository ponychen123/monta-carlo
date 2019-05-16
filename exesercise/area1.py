import numpy as np
import matplotlib.pyplot as plt
import random

f = lambda x: 5*np.sin(6*x)+3*np.sin(2*x)+7
x = np.linspace(0, 10, 1000)
y = f(x)

def compare(point):
    return point[1] <= f(point[0])

#plt.plot(x, y)
#plt.show()

num_points = 100000
rect_width = 10
rect_height = 14

rand_x = lambda: random.uniform(0, rect_width)
rand_y = lambda: random.uniform(0, rect_height)
points_under = []
points = [(rand_x(), rand_y()) for i in range(num_points)]
#must use tuple or the list function do not support
for point in points:
    if compare(point) == True:
        points_under.append(point)
points_above = list(set(points) - set(points_under))

under_x, under_y = zip(*list(points_under))
over_x, over_y = zip(*points_above)

fig = plt.figure()
fig.set_size_inches(12, 8)
plt.scatter(under_x, under_y, s=1, color='red')
plt.scatter(over_x, over_y, s=1, color='green')
plt.show()
