from numpy import *


def lorentz_factor(beta):
    return 1/math.sqrt(1-beta**2)


def p2v(momentum):
    return math.sqrt(1-1/(momentum**2))


# Defining particles
class Electron:
    type = 'electron'
    trace = 'g-'
    mass = 0.511  # MeV

    def __init__(self, energy, direction, position):
        self.position = position  # 1/MeV
        self.direction = direction
        self.energy = energy  # MeV
        self.momentum = sqrt(self.energy ** 2 - self.mass ** 2)

    def evolution(self, mfp):
        self.final_position = self.position + mfp * self.direction
        self.xs = array([self.position[0], self.final_position[0]])
        self.ys = array([self.position[1], self.final_position[1]])
        self.zs = array([self.position[2], self.final_position[2]])


class Positron:
    type = 'positron'
    trace = 'r-'
    mass = 0.511  # MeV

    def __init__(self, energy, direction, position):
        self.position = position  # 1/MeV
        self.direction = direction
        self.energy = energy  # MeV
        self.momentum = sqrt(self.energy ** 2 - self.mass ** 2)

    def evolution(self, mfp):
        self.final_position = self.position + mfp * self.direction
        self.xs = array([self.position[0], self.final_position[0]])
        self.ys = array([self.position[1], self.final_position[1]])
        self.zs = array([self.position[2], self.final_position[2]])

class Photon:
    type = 'photon'
    trace = 'y--'
    mass = 0

    def __init__(self, energy, direction, position):
        self.position = position  # 1/MeV
        self.direction = direction
        self.energy = energy  # MeV
        self.momentum = energy

    def evolution(self, mfp):
        self.final_position = self.position + mfp * self.direction
        self.xs = array([self.position[0], self.final_position[0]])
        self.ys = array([self.position[1], self.final_position[1]])
        self.zs = array([self.position[2], self.final_position[2]])
