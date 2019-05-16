#Numerical Intergration using Monte Carlo method

import math
import random

def f(x):
    return math.sin(x)

xmin = 2.0
xmax = 2.0 + math.pi

numsteps = 1000000
ymin = f(xmin)
ymax = ymin
for i in range(numsteps):
    x = xmin + (xmax - xmin)*float(i)/numsteps
    y = f(x)
    if y < ymin:
        ymin = y
    if y > ymax:
        ymax = y

#Monta Corlo
rectArea = (xmax - xmin)*(ymax - ymin)
numpoints = 1000000
ctr = 0
for j in range(numpoints):
    x = xmin + (xmax - xmin)*random.random()
    y = ymin + (ymax - ymin)*random.random()
    if math.fabs(y) <= math.fabs(f(x)):
        if y > 0 and y <= f(x):
            ctr += 1
        if y < 0 and y >= f(x):
            ctr -= 1
fnarea = rectArea*float(ctr)/numpoints
print("Numerical integration = " + str(fnarea))

