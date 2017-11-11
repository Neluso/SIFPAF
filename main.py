from plot import *
from beam_defaults import *
from time import sleep


# Simulation defaults
e0 = 100  # MeV
beam_dir = array([1, 0, 0])
particles = he_electron(e0, beam_dir)  # For default beams see "beam_defaults.py
sim_config = False
sim_done = False


# Simulation block
def run_simulation(particles):
    fh5 = File('data.h5', 'w', driver=None)
    grp = fh5.create_group('particles')
    stage_number = 0
    particle_num = 0
    multiplicity = 0
    for particle in particles:
        particle.evolution(mfp(e0))
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
    return True


def config_menu():
    initial_paricles = list()
    particle_type = input('SIFPAF ')
    return initial_paricles


help_fh = open('interface.txt', 'r')
for line in help_fh:
    print(line, end='')
help_fh.close()
print()
print()
sleep(1)
while True:
    option = input('SIFPAF> ')
    if option == 'ajuda':
        help_fh = open('interface.txt', 'r')
        for line in help_fh:
            print(line, end='')
        help_fh.close()
    elif option == 'simula':
        if sim_config == False:
            print('No s\'ha configurat cap cas, utilitzant cas per defecte')
            sim_done = run_simulation(particles)
        print('Simulació completada, s\'ha creat el fixer "data.h5')
    elif option == 'mostra':
        if sim_done == False:
            print('No s\'ha fet cap simulació, no es pot mostrar')
        else:
            launch_plots()
    elif option == 'eixir':
        break
    elif option == 'configura':
        particles = config_menu()
    else:
        print('Sentència no vàlida, escriu \"ajuda\" per mostrar controls')
