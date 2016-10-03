import randomVector
import matplotlib.pyplot as plt

#  Definim el nombre d'events
Nevents = 100
Rad = 1
#  Creem els events
def generateEvents(Nev):
    for i in range(Nev):
        vect = randomVector.Vect3D(Rad)
        plt.arrow(0, 0, vect[0], vect[1],length_includes_head=True,width=0.001*Rad)
        axes = plt.gca()
        axes.set_xlim([-Rad,Rad])
        axes.set_ylim([-Rad,Rad])

generateEvents(Nevents)
plt.show()
