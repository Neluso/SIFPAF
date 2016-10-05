import particles
import numpy as np


def emDiffusion(partA, partB):
    pS = np.dot(partA.momentum,partB.momentum)
    s = np.dot(pS,pS)