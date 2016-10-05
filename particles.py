import numpy as np
import math
import relativity as rel

# Defining particles
class Electron:
    mass = 0.511  # MeV
    position = np.array([0,0])  # 1/MeV

    def __init__(self, energy):
        self.energy  # MeV
        maxMomentum = math.sqrt(energy ** 2 - self.mass ** 2)
        self.momentum = np.array([maxMomentum,0])

    def evolution(self,dt):
        pMod = math.sqrt(np.dot(self.momentum,self.momentum))
        vMod = rel.p2v(pMod)
        v = vMod*self.momentum/pMod
        for i in [0,1]:
            self.position[i] = v[i] * dt


class Proton:
    mass = 938.272  # MeV
    position = np.array([0,0])

    def __init__(self, energy):
        self.energy  # MeV
        maxMomentum = math.sqrt(energy ** 2 - self.mass ** 2)
        self.momentum = np.array([maxMomentum, 0])

    def evolution(self,dt):
        pMod = math.sqrt(np.dot(self.momentum,self.momentum))
        vMod = rel.p2v(pMod)
        v = vMod*self.momentum/pMod
        for i in [0,1]:
            self.position[i] = v[i] * dt
