import randomVector
import matplotlib.pyplot as plt

#  Definim el nombre d'events
Nevents = 100

#  Creem els events
for i in range(Nevents):
    vect = randomVector.randomVector()
    plt.arrow(0, 0, vect[0], vect[1])
    axes = plt.gca()
    axes.set_xlim([-1,1])
    axes.set_ylim([-1,1])


plt.show()
