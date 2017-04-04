from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from particle import *
from interactions import *
from tqdm import trange, tqdm


e0 = 100  # MeV


def stage(parts):
    stage_particles = list()
    for part in parts:  #tqdm(parts):
        epsilon = random.rand()
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


# Initializing simulation
beam_dir = array([1, 0, 0])  # isotrope()
particles = [Electron(e0, beam_dir, array([0, 0, 0]))]  #, Positron(e0, - beam_dir, array([0, 0, 0]))]
for particle in particles:
    particle.evolution(mfp())
plot3d = plt.figure('3D Plot')
lng_dev = plt.figure('Logitudinal developement')
yz_plane = plt.figure('Transverse developement')
ax_plot3d = plot3d.add_subplot(111, projection='3d')
ax_xy_lng_dev = lng_dev.add_subplot(211)
ax_xz_lng_dev = lng_dev.add_subplot(212)
ax_yz_plane = yz_plane.add_subplot(111)
stage_number = 0
multiplicity = 0
fh = open('sim_file.txt', 'w')


# Simulation block
for stage_number in trange(10):  # stops at 600 keV
    fh.write('Stage number: ' + str(stage_number) + '\n\n')
    for particle in particles:
        ax_plot3d.plot(particle.xs, particle.ys, particle.zs, particle.trace)
        ax_xy_lng_dev.plot(particle.xs, particle.ys, particle.trace)
        ax_xz_lng_dev.plot(particle.xs, particle.zs, particle.trace)
        ax_yz_plane.plot(particle.ys, particle.zs, particle.trace)
        fh.write('Particle type: ' + particle.type + '\n')
        fh.write('Particle energy: ' + str(particle.energy) + '\n')
        fh.write('Particle momentum: ' + str(particle.momentum) + '\n\n')
    particles = stage(particles)
    checker = range(len(particles))
    for i in checker:
        try:
            particles.remove(None)
        except:
            None
    for i in range(len(particles) - 1):
        if particles[i].type is not 'photon':
            if particles[i].energy <= 0.511:
                particles[i] = particles[i + 1]
    if particles[-1] is not 'photon':
        if particles[-1].energy <= 0.511:
            del particles[-1]
    if len(particles) == multiplicity: break
    fh.write('\nParticle number in this stage:' + str(multiplicity) + '\n\n\n\n\n')
    multiplicity = len(particles)
fh.close()


# Debugging purposes
print(particles)
shower_axis = zeros(3)
for particle in particles:
    shower_axis += particle.final_position
shower_axis /= len(particles)
ax_plot3d.plot((0, shower_axis[0]), (0, shower_axis[1]), (0, shower_axis[2]), 'k-')
ax_xy_lng_dev.plot((0, shower_axis[0]), (0, shower_axis[1]), 'k-')
ax_xz_lng_dev.plot((0, shower_axis[0]), (0, shower_axis[2]), 'k-')
ax_yz_plane.plot((0, shower_axis[1]), (0, shower_axis[2]), 'k-')



# Plotting results and images
ax_plot3d.set_title('3D Plot')
ax_plot3d._axis3don = False
ax_xy_lng_dev.set_ylabel('y')
ax_xz_lng_dev.set_ylabel('z')
lng_dev.suptitle('Longitudinal developement')
ax_xz_lng_dev.set_xlabel('x')
lng_dev.savefig('long_dev.jpg')
yz_plane.savefig('trans_plane.jpg')
plt.show()