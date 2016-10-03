import randomVector
import matplotlib.pyplot as plt

#  Definim el nombre d'events
Nevents = 100

#  Creem els events
def generateEvents(Nev):
    for i in range(Nev):
        vect = randomVector.Vect3D()
        plt.arrow(0, 0, vect[0], vect[1])
        axes = plt.gca()
        axes.set_xlim([-1,1])
        axes.set_ylim([-1,1])

generateEvents(Nevents)
plt.show()
