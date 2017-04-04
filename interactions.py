from numpy import *
from particle import *


momentum_cut = 0.04  # MeV -> 40 keV


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
    n /= linalg.norm(n)
    return cos(ang) * direct + sin(ang) * n


def scattering(part):
    if part.momentum_norm < momentum_cut:
        part.momentum = 0
        part.evolution(mfp())
        return part
    inter_energy = part.energy * 0.9
    inter_direction = new_direction(part.direction, 0.01)
    inter_position = part.final_position
    if part.type is 'electron':
        new_part = Electron(inter_energy, inter_direction, inter_position)
        new_part.evolution(mfp())
        return new_part
    elif part.type is 'positron':
        new_part = Positron(inter_energy, inter_direction, inter_position)
        new_part.evolution(mfp())
        return new_part


def brehmstrallung(part):
    inter_energy_q = part.energy * (random.rand() * 0.2 + 0.4)  # TODO: Bethe-Block -> energy loss
    inter_energy_ph = part.energy - inter_energy_q
    inter_position = part.final_position
    inter_direction_q = new_direction(part.direction, 0.01)  # TODO: diff. cross sect. -> angular distribution
    if part.type is 'electron':
        new_part = Electron(inter_energy_q, inter_direction_q, inter_position)
    elif part.type is 'positron':
        new_part = Positron(inter_energy_q, inter_direction_q, inter_position)
    inter_direction_ph = part.momentum - new_part.momentum
    inter_direction_ph /= linalg.norm(inter_direction_ph)
    new_photon = Photon(inter_energy_ph, inter_direction_ph, inter_position)
    new_part.evolution(mfp())
    new_photon.evolution(mfp())
    return [new_part, new_photon]


def pair_production(part):
    inter_energy = part.energy / 2  # TODO: photon trough matter -> energy loss
    inter_direction_pos = new_direction(part.direction, 0.01)
    inter_position = part.final_position
    new_positron = Positron(inter_energy, inter_direction_pos, inter_position)
    inter_direction_neg = part.momentum - new_positron.momentum
    inter_direction_neg /= linalg.norm(inter_direction_neg)
    new_electron = Electron(inter_energy, inter_direction_neg, inter_position)
    new_positron.evolution(mfp())
    new_electron.evolution(mfp())
    return [new_electron, new_positron]


def annihilation(part):
    inter_position = part.final_position
    inter_energy = part.energy / 2
    if part.momentum_norm < momentum_cut:
        inter_direction = isotrope()
        photon_pos = Photon(inter_energy, inter_direction, inter_position)
        photon_neg = Photon(inter_energy, - inter_direction, inter_position)
    else:
        inter_direction_pos = new_direction(part.direction, 0.01)
        photon_pos = Photon(inter_energy, inter_direction_pos, inter_position)
        inter_direction_neg = part.momentum - photon_pos.momentum
        inter_direction_neg /= linalg.norm(inter_direction_neg)
        photon_neg = Photon(inter_energy, inter_direction_neg, inter_position)
    photon_pos.evolution(mfp())
    photon_neg.evolution(mfp())
    return [photon_pos, photon_neg]


def photoelectric(part):
    inter_energy = 0.9 * part.energy
    inter_direction = part.direction
    inter_position = part.final_position
    el = Electron(inter_energy, inter_direction, inter_position)
    el.evolution(mfp())
    return el