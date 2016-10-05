#  Author: Neluso
#  Main
import matplotlib.pyplot as plt
import numpy as np
import math
import random


#  Defining Utils for execution
def Vect2D(Energy):
    Rad = np.random.normal(Energy,0.1)
    theta = -math.pi/2 + math.pi * random.random()
    x = Rad * math.cos(theta)
    y = Rad * math.sin(theta)
    return np.array([x, y])


def generateEvents(Nev, Ener):
    vectAux = np.array([0,0])
    for i in range(Nev):
        vect = Vect2D(Ener)
        plt.arrow(vectAux[0], vectAux[1], vect[0], vect[1],length_includes_head=True,width=0.0008*Ener)
        vectAux = vect


#  Defining Beam
while True:
    break #  for the moment this remains inactive
    try:
        Intensity = float(input("Intensitat del feix (partícules/s) = "))
        Energy = int(input("Energia del feix (Mev) = "))
        break
    except:
        input("Ha ocorregut un error, polse una tecla per continuar.")
        continue

Nevents = 10  #  -> Intensity
Energy = 1.   # This would be removed

#  Create events


generateEvents(Nevents,Energy)

axes = plt.gca()
axes.set_xlim([0,Energy])
axes.set_ylim([-Energy,Energy])
plt.show()
