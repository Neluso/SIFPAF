import matplotlib.pyplot as plt
from h5py import File
from numpy import array


def launch_plots():  # TODO set activation of different plots
    plot3d = plt.figure('Plot 3D')
    lng_dev = plt.figure('Desenvolupament longitudinal')
    yz_plane = plt.figure('Desenvolupament transversal')
    ax_plot3d = plot3d.add_subplot(111, projection='3d')
    ax_xy_lng_dev = lng_dev.add_subplot(211)
    ax_xz_lng_dev = lng_dev.add_subplot(212)
    ax_yz_plane = yz_plane.add_subplot(111)
    ax_plot3d.set_title('3D Plot')
    ax_plot3d._axis3don = False
    ax_xy_lng_dev.set_ylabel('y')
    ax_xz_lng_dev.set_ylabel('z')
    lng_dev.suptitle('Longitudinal development')
    ax_xz_lng_dev.set_xlabel('x')
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
        ax_xy_lng_dev.plot(xs, ys, trace)
        ax_xz_lng_dev.plot(xs, zs, trace)
        ax_yz_plane.plot(ys, zs, trace)
    lng_dev.savefig('long_dev.jpg')
    yz_plane.savefig('trans_plane.jpg')
    plt.show()
