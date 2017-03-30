from numpy import *
from particle import Electron, Photon, Positron


e0 = 1000  # MeV


def stage(parts, e_n):
    stage_particles = list()
    for part in parts:
        if part.type is 'electron':
            stage_particles.append(Electron(e_n))
            stage_particles.append(Photon(e_n))
        elif part.type is 'positron':
            stage_particles.append(Photon(e_n))
            stage_particles.append(Photon(e_n))
        elif part.type is 'photon':
            stage_particles.append(Electron(e_n))
            stage_particles.append(Positron(e_n))
    return stage_particles


particles = [Photon(e0)]
while e0 > 1:
    print(particles)
    particles = stage(particles, e0 / 2)
    e0 /= 2
