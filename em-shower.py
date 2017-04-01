from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from particle import *
from interactions import *


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
        ang = 1 / e0
        new_up_dir = new_direction(part.direction, ang)
        new_dn_dir = new_direction(part.direction, - ang)
        if part.type is 'electron':
            brehms = brehmstrallung(part)
            stage_particles.append(brehms[0])
            stage_particles.append(brehms[1])
        elif part.type is 'positron':
            annih = annihilation(part)
            stage_particles.append(annih[0])
            stage_particles.append(annih[1])
        elif part.type is 'photon':
            if part.energy > 1.022:
                pair = pair_production(part)
                stage_particles.append(pair[0])
                stage_particles.append(pair[1])
            else:
                stage_particles.append(Electron(e_n, part.direction, part.final_position))
    return stage_particles


e = e0
beam_dir = array([1, 0, 0])  # isotrope()
particles = [Electron(e, beam_dir, array([0, 0, 0]))]  #, Positron(e0, - beam_dir, array([0, 0, 0]))]
for particle in particles:
    particle.evolution(mfp())
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


while True:  # stops at 600 keV
    for particle in particles:
        ax.plot(particle.xs, particle.ys, particle.zs, particle.trace)
    particles = stage(particles, e / 2)
    e /= 2
    if e / 2 < 0.511: break
plt.show()