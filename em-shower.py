from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from particle import *
from interactions import *


e0 = 100  # MeV


def mfp():
    return random.exponential(1)


# def isotrope():
#     ep1 = random.rand()
#     ep2 = random.rand()
#     theta = arccos(1 - 2 * ep1)
#     phi = 2 * pi * ep2
#     return array([sin(theta) * cos(phi), sin(theta) * sin(phi), cos(theta)])
#
#
# def new_direction(direct, ang):
#     n = cross(direct, isotrope())
#     return cos(ang) * direct + sin(ang) * n


def stage(parts, e_n):
    stage_particles = list()
    for part in parts:
        epsilon = random.rand()
        if part.type is 'electron':
            if part.energy <= 0.511:
                stage_particles.append(scattering(part))
            else:
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
                el = Electron(e_n, part.direction, part.final_position)
                stage_particles.append(el.evolution(mfp()))
    return stage_particles


e = e0
beam_dir = array([1, 0, 0])  # isotrope()
particles = [Electron(e, beam_dir, array([0, 0, 0]))]  #, Positron(e0, - beam_dir, array([0, 0, 0]))]
for particle in particles:
    particle.evolution(mfp())
plot3d = plt.figure('3D Plot')
lng_dev = plt.figure('Logitudinal developement')
yz_plane = plt.figure('Transverse developement')
ax_plot3d = plot3d.add_subplot(111, projection='3d')
ax_xy_lng_dev = lng_dev.add_subplot(211)
ax_xz_lng_dev = lng_dev.add_subplot(212)
ax_yz_plane = yz_plane.add_subplot(111)

while True:  # stops at 600 keV
    print(e, particles)
    e /= 2
    for particle in particles:
        ax_plot3d.plot(particle.xs, particle.ys, particle.zs, particle.trace)
        ax_xy_lng_dev.plot(particle.xs, particle.ys, particle.trace)
        ax_xz_lng_dev.plot(particle.xs, particle.zs, particle.trace)
        ax_yz_plane.plot(particle.ys, particle.zs, particle.trace)
    particles = stage(particles, e)
    if e < 0.511: break


shower_axis = zeros(3)
for particle in particles:
    shower_axis += particle.final_position
shower_axis /= len(particles)
ax_plot3d.plot((0, shower_axis[0]), (0, shower_axis[1]), (0, shower_axis[2]), 'k-')
ax_xy_lng_dev.plot((0, shower_axis[0]), (0, shower_axis[1]), 'k-')
ax_xz_lng_dev.plot((0, shower_axis[0]), (0, shower_axis[2]), 'k-')
ax_yz_plane.plot((0, shower_axis[1]), (0, shower_axis[2]), 'k-')



ax_plot3d.set_title('3D Plot')
ax_plot3d._axis3don = False
ax_xy_lng_dev.set_ylabel('y')
ax_xz_lng_dev.set_ylabel('z')
lng_dev.suptitle('Longitudinal developement')
ax_xz_lng_dev.set_xlabel('x')
plt.show()