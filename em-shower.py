from beam_defaults import *


# Initializing simulation
e0 = 10  # MeV
beam_dir = array([1, 0, 0])
particles = he_electron(e0, beam_dir)  # For default beams see "beam_defaults.py
for particle in particles:
    particle.evolution(mfp(e0))
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
fh5 = File('data.h5', 'w', driver=None)


# Simulation block
while True:  # stops at 600 keV
    num = str(stage_number)
    while True:
        if len(num) < 4:
            num = '0' + num
        else:
            break
    fh.write('Stage number: ' + num + '\n\n')
    grp = fh5.create_group(num + 'stage')

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
        particle_data = grp.create_group(num + '_' + particle.type)
        particle_data.create_dataset('energy', (1,), data=particle.energy)
        particle_data.create_dataset('momentum', particle.momentum.shape, data=particle.momentum)
        particle_data.create_dataset('initial_position', particle.initial_position.shape,
                                     data=particle.initial_position)
        particle_data.create_dataset('final_position', particle.final_position.shape,
                                     data=particle.final_position)
        fh5.flush()
        ax_plot3d.plot(particle.xs, particle.ys, particle.zs, particle.trace)
        ax_xy_lng_dev.plot(particle.xs, particle.ys, particle.trace)
        ax_xz_lng_dev.plot(particle.xs, particle.zs, particle.trace)
        ax_yz_plane.plot(particle.ys, particle.zs, particle.trace)
        fh.write('Particle type: ' + particle.type + '\n')
        fh.write('Particle energy: ' + str(particle.energy) + '\n')
        fh.write('Particle momentum: ' + str(particle.momentum) + '\n\n')
    print('Stage', stage_number)
    particles = stage(particles)
    if len(particles) == multiplicity: break
    fh.write('\nParticle number in this stage:' + str(multiplicity) + '\n\n\n\n\n')
    # print(multiplicity, len(particles))
    multiplicity = len(particles)
    stage_number += 1
fh.close()


# Plotting results and images
ax_plot3d.set_title('3D Plot')
ax_plot3d._axis3don = False
ax_xy_lng_dev.set_ylabel('y')
ax_xz_lng_dev.set_ylabel('z')
lng_dev.suptitle('Longitudinal development')
ax_xz_lng_dev.set_xlabel('x')
lng_dev.savefig('long_dev.eps')
yz_plane.savefig('trans_plane.eps')
plt.show()
