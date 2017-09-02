from numpy import *
from particle import *
from tqdm import tqdm


momentum_cut = 0.04  # MeV -> 40 keV


def mfp(inter_energy):
    return random.exponential(1)


def isotrope(origin=array([0, 0, 0])):
    ep1 = random.rand()
    ep2 = random.rand()
    theta = arccos(1 - 2 * ep1)
    phi = 2 * pi * ep2
    return origin + array([sin(theta) * cos(phi), sin(theta) * sin(phi), cos(theta)])


def new_direction(direct, ang):
    n = cross(direct, isotrope())
    n_norm = linalg.norm(n)
    if n_norm <= 0:
        return cos(ang) * direct + sin(ang) * n
    else:
        n /= n_norm
        return cos(ang) * direct + sin(ang) * n


def scattering(part):
    if part.momentum_norm < momentum_cut:
        return None
    inter_direction = isotrope()
    inter_energy = part.energy * 0.5 * (1 + dot(part.direction, inter_direction))
    inter_position = part.final_position
    if part.type is 'electron':
        new_part = Electron(inter_energy, inter_direction, inter_position)
        new_part.evolution(mfp(inter_energy))
        return new_part
    elif part.type is 'positron':
        new_part = Positron(inter_energy, inter_direction, inter_position)
        new_part.evolution(mfp(inter_energy))
        return new_part


def brehmstrallung(part):
    if part.momentum_norm < momentum_cut:
        return [part, None]
    inter_energy_q = part.energy * (random.rand() * 0.2 + 0.4)  # TODO: Bethe-Block -> energy loss
    inter_energy_ph = part.energy - inter_energy_q
    inter_position = part.final_position
    inter_direction_q = new_direction(part.direction, 0.01)  # TODO: diff. cross sect. -> angular distribution
    if part.type is 'electron':
        new_part = Electron(inter_energy_q, inter_direction_q, inter_position)
    elif part.type is 'positron':
        new_part = Positron(inter_energy_q, inter_direction_q, inter_position)
    inter_direction_ph = part.momentum - new_part.momentum
    ph_dir_norm = linalg.norm(inter_direction_ph)
    if ph_dir_norm > 0:
        inter_direction_ph /= ph_dir_norm
    else:
        inter_direction_ph = zeros(3)
    new_photon = Photon(inter_energy_ph, inter_direction_ph, inter_position)
    new_part.evolution(mfp(inter_energy_q))
    new_photon.evolution(mfp(inter_energy_ph))
    return [new_part, new_photon]


def pair_production(part):
    if part.momentum_norm < momentum_cut:
        return None
    inter_energy = part.energy / 2  # TODO: photon trough matter -> energy loss
    inter_direction_pos = new_direction(part.direction, 0.01)
    inter_position = part.final_position
    new_positron = Positron(inter_energy, inter_direction_pos, inter_position)
    inter_direction_neg = part.momentum - new_positron.momentum
    inter_direction_neg /= linalg.norm(inter_direction_neg)
    new_electron = Electron(inter_energy, inter_direction_neg, inter_position)
    new_positron.evolution(mfp(inter_energy))
    new_electron.evolution(mfp(inter_energy))
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
    photon_pos.evolution(mfp(inter_energy))
    photon_neg.evolution(mfp(inter_energy))
    return [photon_pos, photon_neg]


def photoelectric(part):
    if part.momentum_norm < momentum_cut:
        return None
    inter_energy = 0.9 * part.energy
    inter_direction = part.direction
    inter_position = part.final_position
    if inter_energy < 0.511:
        el = Electron(0, inter_direction, inter_position)
    else:
        el = Electron(inter_energy, inter_direction, inter_position)
    el.evolution(mfp(inter_energy))
    return el


def stage(parts):
    stage_particles = list()
    for part in tqdm(parts):
        if part.momentum_norm <= momentum_cut:
            continue
        epsilon = 0.5  # random.rand()
        if part.type is 'electron':
            if epsilon > 0.1:
                brehms = brehmstrallung(part)
                stage_particles.append(brehms[0])
                stage_particles.append(brehms[1])
            else:
                stage_particles.append(scattering(part))
        elif part.type is 'positron':
            if epsilon > 0.1:
                annih = annihilation(part)
                stage_particles.append(annih[0])
                stage_particles.append(annih[1])
            else:
                stage_particles.append(scattering(part))
        elif part.type is 'photon':
            if part.energy >= 1.022:
                pair = pair_production(part)
                stage_particles.append(pair[0])
                stage_particles.append(pair[1])
            else:
                stage_particles.append(photoelectric(part))
    return stage_particles