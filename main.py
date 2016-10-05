#  Author: Neluso
#  Main
import matplotlib.pyplot as plt
import numpy as np
import math
import random

#  Defining Utils for execution
def Vect2D(Energy):
    Rad = np.random.normal(Energy,0.1*Energy)
    theta = np.random.normal(0,0.01)
    x = Rad * math.cos(theta)
    y = Rad * math.sin(theta)
    return np.array([[x, y]])


def generateEvents(Ener):
    vect = np.ones((0,2))
    dEner = 0.1*Ener #  that will be a function which will return the energy loss computed with an interaction probability
    while Ener > 0:
        vect=np.append(vect,Vect2D(Ener),axis=0)
        Ener -= dEner
    return vect


def setTrajectory(vect):
    nEv = vect.shape[0]
    traject = np.zeros((nEv+1,2))
    for i in range(nEv+1):
        element = [np.sum(vect[0:i,0]),np.sum(vect[0:i,1])]
        traject[i,:] = element
    return traject


def drawTrajectory(traject):
    nEv = traject.shape[0]
    for i in range(nEv):
        plt.plot(traject[0:i,0], traject[0:i,1],'-b')


def particle(Energy):
    events = generateEvents(Energy)
    tr = setTrajectory(events)
    drawTrajectory(tr)


#  Defining Beam
def readBeam():
    while True:
        try:
            Intensity = float(input("Intensitat del feix (partícules/s) = "))
            Energy = int(input("Energia del feix (Mev) = "))
            break
        except:
            input("Ha ocorregut un error, polse una tecla per continuar.")
            continue
    return Intensity, Energy


Nevents = 1000  #  -> Intensity
Energy = 1000.   # This would be removed

#  Create events



axes = plt.gca()
axes.axis('auto')

for i in range(Nevents):
    print('Calculating particle',i+1)
    particle(np.random.normal(Energy,1))

plt.show()

