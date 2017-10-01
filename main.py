# select menu


#
from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from particle import *
from interactions import *
from tqdm import trange, tqdm
from h5py import File
from plot import *
from beam_defaults import *


# Initializing simulation
e0 = 100  # MeV
beam_dir = array([1, 0, 0])
particles = he_electron(100, beam_dir)  # For default beams see "beam_defaults.py
for particle in particles:
    particle.evolution(mfp(e0))
stage_number = 0
multiplicity = 0
particle_num = 0
fh5 = File('data.h5', 'w', driver=None)
grp = fh5.create_group('particles')


# Simulation block
while True:  # stops at 600 keV
    if len(particles) == 0:
        break
    for particle in particles:
        if particle is None:
            continue
        if particle.momentum_norm == 0:
            continue
        particle_num += 1
        particle_data = grp.create_group(str(particle_num))
        particle_data.create_dataset('energy', (1,), data=particle.energy)
        particle_data.create_dataset('momentum', particle.momentum.shape, data=particle.momentum)
        particle_data.create_dataset('initial_position', particle.initial_position.shape,
                                     data=particle.initial_position)
        particle_data.create_dataset('final_position', particle.final_position.shape,
                                     data=particle.final_position)
        particle_data.create_dataset('trace', (1,), data=particle.trace)
    particles = stage(particles)
    if len(particles) == multiplicity: break
    multiplicity = len(particles)
    stage_number += 1


launch_plots()
