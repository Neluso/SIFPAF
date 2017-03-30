from numpy import *
from particle import Electron, Foton, Positron


e0 = 10  # MeV


particles = [Electron(e0)]
stage = 0
while e0 > 1:
    if particles[stage].type is 'electron':
        particles.append(Electron(e0 / 2).type)
        particles.append(Foton(e0 / 2).type)
    elif particles[stage].type is 'positron':
        particles.append(Foton(e0 / 2).type)
        particles.append(Foton(e0 / 2).type)
    elif particles[stage] is 'photon':
        particles.append(Electron[e0 / 2].type)
        particles.append(Positron[e0 / 2].type)
    stage += 1
    e0 /= 2
print(particles)