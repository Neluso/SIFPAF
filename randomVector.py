import numpy as np
import random
import math


def Vect2D(Energy):
    Rad = np.random.normal(Energy,0.1)
    theta = -math.pi/2 + math.pi * random.random()
    x = Rad * math.cos(theta)
    y = Rad * math.sin(theta)
    return np.array([x, y])
