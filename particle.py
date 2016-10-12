import numpy as np
import math


def lorentz_factor(beta):
    return 1/math.sqrt(1-beta**2)


def p2v(momentum):
    return math.sqrt(1-1/(momentum**2))


# Defining particles
class Electron:
    mass = 0.511  # MeV
    position = np.array([0,0])  # 1/MeV

    def __init__(self, energy):
        self.energy = float(energy)
        self.energy = energy  # MeV
        maxMomentum = math.sqrt(energy ** 2 - self.mass ** 2)
        self.momentum = np.array([maxMomentum,0])

    def evolution(self, dt):
        pModule = math.sqrt(np.dot(self.momentum,self.momentum))
        vModule = p2v(pModule)
        v = vModule * self.momentum / pModule
        self.position =  v * dt


################################
#  By the moment just working on first type of particles (Electrons)
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


class Foton:
    mass = 0