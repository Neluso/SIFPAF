from numpy import *
from matplotlib.pyplot import plot, show
from particle import Electron, Photon, Positron


e0 = 100  # MeV


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


def stage(parts, e_n):
    stage_particles = list()
    for part in parts:
        new_up_dir = new_direction(part.direction, 0.1)
        new_dn_dir = new_direction(part.direction, - 0.1)
        if part.type is 'electron':
            stage_particles.append(Electron(e_n, new_up_dir, part.final_position))
            stage_particles.append(Photon(e_n, new_dn_dir, part.final_position))
        elif part.type is 'positron':
            stage_particles.append(Photon(e_n, new_up_dir, part.final_position))
            stage_particles.append(Photon(e_n, new_dn_dir, part.final_position))
        elif part.type is 'photon':
            if part.energy > 1.022:
                stage_particles.append(Electron(e_n, new_up_dir, part.final_position))
                stage_particles.append(Positron(e_n, new_dn_dir, part.final_position))
            else:
                stage_particles.append(Electron(e_n, part.direction, part.final_position))
    evolved_particles = list()
    for part in stage_particles:
        evolved_particles.append(part.evolution(mfp()))
    return stage_particles


beam_dir = isotrope()
particles = [Electron(e0, beam_dir, array([0, 0, 0])), Positron(e0, - beam_dir, array([0, 0, 0]))]
while True:  # stops at 600 keV
    print(particles)
    for particle in particles:
        particle.evolution(mfp())
        plot(particle.xs, particle.ys, particle.trace)
    particles = stage(particles, e0 / 2)
    e0 /= 2
    if e0 / 2 < 0.511: break
show()