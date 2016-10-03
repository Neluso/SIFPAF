import random
import numpy as np


def Vect2D(Rad):
    x = -Rad + 2 * Rad * random.random()
    y = -Rad + 2 * Rad * random.random()
    return np.array([x, y])


def Vect3D(Rad):
    x = -Rad + 2 * Rad * random.random()
    y = -Rad + 2 * Rad * random.random()
    z = -Rad + 2 * Rad * random.random()
    return np.array([x, y , z])
