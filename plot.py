import matplotlib.pyplot as plt
from h5py import File
from numpy import array


def launch_plots():  # TODO set activation of different plots
    plot3d = plt.figure('Plot 3D')
    xy_plane = plt.figure('XY')
    xz_plane = plt.figure('XZ')
    yz_plane = plt.figure('YZ')
    ax_plot3d = plot3d.add_subplot(111, projection='3d')
    ax_xy = xy_plane.add_subplot(111)
    ax_xz = xz_plane.add_subplot(111)
    ax_yz = yz_plane.add_subplot(111)
    ax_plot3d.set_title('3D')
    ax_plot3d._axis3don = False
    ax_xy.set_ylabel('y')
    ax_xy.set_xlabel('x')
    ax_xz.set_ylabel('z')
    ax_xz.set_xlabel('x')
    ax_yz.set_ylabel('z')
    ax_yz.set_xlabel('y')
    fh5 = File('data.h5', 'r')
    total_particles = len(list(fh5['/particles'])) + 1
    for particle_count in range(1, total_particles):
        route = '/particles/' + str(particle_count) + '/'
        trace = fh5[route + 'trace'].value[0]
        initial_position = fh5[route + 'initial_position']
        final_position = fh5[route + 'final_position']
        xs = array([initial_position[0], final_position[0]])
        ys = array([initial_position[1], final_position[1]])
        zs = array([initial_position[2], final_position[2]])
        ax_plot3d.plot(xs, ys, zs, trace)
        ax_xy.plot(xs, ys, trace)
        ax_xz.plot(xs, zs, trace)
        ax_yz.plot(ys, zs, trace)
    xy_plane.savefig('XY.jpg')
    xz_plane.savefig('XZ.jpg')
    yz_plane.savefig('YZ.jpg')
    plt.show()
