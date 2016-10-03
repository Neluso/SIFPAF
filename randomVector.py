import random
import numpy as np



def randomVector():
    x = -1 + 2 * random.random()
    y = -1 + 2 * random.random()
    z = -1 + 2 * random.random()
    return np.array([x * random.random(), y * random.random(), z * random.random()])

