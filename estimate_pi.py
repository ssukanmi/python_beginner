"""
Estimating the value of pi 
Using ratio of (points in a circle inscribed in a square / total points in the square)
pi * r^2 / (2 * r)^2
cross mulitplying and chagning of subject will result to
pi = (4 * points in circle) / total points
"""

import random
import matplotlib.pyplot as plt


def estimate_pi(n):
    x_values = []
    y_values = []
    points_in_cirlcle = 0
    points_in_total = 0
    for x in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        x_values.append(x)
        y_values.append(y)
        # if dist <= 1, then the point  is in the circle
        dist = x**2 + y**2
        if dist <= 1:
            points_in_cirlcle += 1
        points_in_total += 1

    print(4 * points_in_cirlcle/points_in_total)
    return x_values, y_values


arc_x = [i*0.001 for i in range(1001)]
arc_y = [(1 - i**2)**0.5 for i in arc_x]
x, y = estimate_pi(10000)

plt.figure(figsize=(10, 10))
plt.plot(x, y, linestyle='', marker='*', label='scatter points')
plt.plot(arc_x, arc_y, label='circle arc', color='r')
plt.legend()
plt.title('Estimation of pi using a scatter plot')

plt.show()
