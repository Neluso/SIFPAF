from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from particle import *
from interactions import *
from tqdm import trange, tqdm
from h5py import File


def b2b_photon(e0):
    beam_dir = isotrope()
    return [Photon(e0, beam_dir, array([0, 0, 0])), Photon(e0, - beam_dir, array([0, 0, 0]))]


def he_electron(e0, beam_dir):
    return [Electron(e0, beam_dir, array([0, 0, 0]))]


def beta_emiter_spherical(n_beta=10, center=array([0, 0, 0]), radius=1):
    particles = list()
    for i in range(n_beta):
        beam_dir = isotrope()
        init_pos = isotrope(origin=center)
        particles.append(Photon(0.511, beam_dir, radius * init_pos))
        particles.append(Photon(0.511, - beam_dir, radius * init_pos))
    return particles


def beta_emiter_cube(n_beta=10, cube_center=array([0, 0, 0]), cube_side=1):
    particles = list()
    cubeLimits = list()
    cube_side /= 2
    for i in range(n_beta):
        beam_dir = isotrope()
        init_pos = isotrope()

        particles.append(Photon(0.511, beam_dir, init_pos))
        particles.append(Photon(0.511, -beam_dir, init_pos))
