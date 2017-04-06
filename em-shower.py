from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from particle import *
from interactions import *
from tqdm import trange, tqdm
from h5py import File


#########################################





#########################################


# Initializing simulation
e0 = 100  # MeV
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
fh5 = File('data.h5', 'w')


# Simulation block
while True:  # stops at 600 keV
    num = str(stage_number)
    while True:
        if len(num) < 4:
            num = '0' + num
        else:
            break
    fh.write('Stage number: ' + num + '\n\n')
    grp = fh5.create_group('Stage ' + num)
    part_num = 0
    if len(particles) == 0:
        break
    for particle in particles:
        if particle is None:
            continue
        if particle.momentum_norm == 0:
            continue
        part_num += 1
        num = str(part_num)
        while True:
            if len(num) < 4:
                num = '0' + num
            else:
                break
        particle_data = grp.create_group(num + ' ' + particle.type)
        particle_data.create_dataset('energy', (1,), data=particle.energy)
        particle_data.create_dataset('momentum', particle.momentum.shape, data=particle.momentum)
        particle_data.create_dataset('initial_position', particle.initial_position.shape,
                                     data=particle.initial_position)
        particle_data.create_dataset('final_position', particle.final_position.shape,
                                     data=particle.final_position)
        ax_plot3d.plot(particle.xs, particle.ys, particle.zs, particle.trace)
        ax_xy_lng_dev.plot(particle.xs, particle.ys, particle.trace)
        ax_xz_lng_dev.plot(particle.xs, particle.zs, particle.trace)
        ax_yz_plane.plot(particle.ys, particle.zs, particle.trace)
        fh.write('Particle type: ' + particle.type + '\n')
        fh.write('Particle energy: ' + str(particle.energy) + '\n')
        fh.write('Particle momentum: ' + str(particle.momentum) + '\n\n')
    try:
        particles = stage(particles)
    except:
        print('End of simulation')
    if len(particles) == multiplicity: break
    fh.write('\nParticle number in this stage:' + str(multiplicity) + '\n\n\n\n\n')
    print(multiplicity, len(particles))
    multiplicity = len(particles)
    stage_number += 1
fh.close()


# Debugging purposes
# print(particles)
# shower_axis = zeros(3)
# for particle in particles:
#     shower_axis += particle.final_position
# shower_axis /= len(particles)
# ax_plot3d.plot((0, shower_axis[0]), (0, shower_axis[1]), (0, shower_axis[2]), 'k-')
# ax_xy_lng_dev.plot((0, shower_axis[0]), (0, shower_axis[1]), 'k-')
# ax_xz_lng_dev.plot((0, shower_axis[0]), (0, shower_axis[2]), 'k-')
# ax_yz_plane.plot((0, shower_axis[1]), (0, shower_axis[2]), 'k-')



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
