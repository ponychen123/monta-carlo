import matplotlib.pyplot as plt
import numpy as np

def buffons_needle():
    N = 10**5
    
    x1 = 9*np.random.rand(1, N) + 1
    y1 = 9*np.random.rand(1, N) + 1

    theta = 2*np.pi*np.random.rand(1, N)

    x2 = x1 + np.cos(theta)
    y2 = y1 + np.sin(theta)

    criterion = np.ceil(np.minimum(y1, y2)) == np.floor(np.maximum(y1, y2)) 

    numwins = np.sum(criterion)

    p = numwins/N
    print("the probability that a needle intersects a line is approximately %9.6f\n", p)
    
    index = range(300)
    plt.plot([x1[0][index], x2[0][index]], [y1[0][index], y2[0][index]], '-')
    plt.axis([0, 11, 0, 11])
    plt.xticks(range(12))
    plt.yticks(range(12))
    plt.gca().yaxis.grid(True)
    plt.show()

buffons_needle()

