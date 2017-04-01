from numpy import *
from particle import *


def mfp():
    return random.exponential(1)


def isotrope():
    ep1 = random.rand()
    ep2 = random.rand()
    theta = arccos(1 - 2 * ep1)
    phi = 2 * pi * ep2
    return array([sin(theta) * cos(phi), sin(theta) * sin(phi), cos(theta)])


def new_direction(direct, ang):
    n = cross(direct, isotrope())
    return cos(ang) * direct + sin(ang) * n


def scattering(part):
    inter_energy = part.energy / 2
    inter_direction_pos = new_direction(part.direction, 0.01)
    inter_direction_neg = new_direction(part.direction, - 0.01)
    inter_position = part.final_position
    return None  # to define


def brehmstrallung(part):
    inter_energy = part.energy / 2
    inter_direction_pos = new_direction(part.direction, 0.01)
    inter_direction_neg = new_direction(part.direction, - 0.01)
    inter_position = part.final_position
    new_photon = Photon(inter_energy, inter_direction_neg, inter_position)
    if part.type is 'electron':
        new_part = Electron(inter_energy, inter_direction_pos, inter_position)
    elif part.type is 'positron':
        new_part = Positron(inter_energy, inter_direction_pos, inter_position)
    new_part.evolution(mfp())
    new_photon.evolution(mfp())
    return [new_part, new_photon]


def pair_production(part):
    inter_energy = part.energy / 2
    inter_direction_pos = new_direction(part.direction, 0.01)
    inter_direction_neg = new_direction(part.direction, - 0.01)
    inter_position = part.final_position
    new_positron = Positron(inter_energy, inter_direction_pos, inter_position)
    new_electron = Electron(inter_energy, inter_direction_neg, inter_position)
    new_positron.evolution(mfp())
    new_electron.evolution(mfp())
    return [new_electron, new_positron]


def annihilation(part):
    inter_energy = part.energy / 2
    inter_direction_pos = new_direction(part.direction, 0.01)
    inter_direction_neg = new_direction(part.direction, - 0.01)
    inter_position = part.final_position
    photon_pos = Photon(inter_energy, inter_direction_pos, inter_position)
    photon_neg = Photon(inter_energy, inter_direction_neg, inter_position)
    photon_pos.evolution(mfp())
    photon_neg.evolution(mfp())
    return [photon_pos, photon_neg]