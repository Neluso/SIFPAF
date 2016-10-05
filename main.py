#  Author: Neluso
#  Main
import matplotlib.pyplot as plt
import numpy as np
import math


# Defining relativity convertions
def lorentz_factor(beta):
    return 1/math.sqrt(1-beta**2)


def p2v(momentum):
    return  math.sqrt(1-1/(momentum**2))


# Defining particles
class Electron:
    mass = 0.511  # MeV
    position = np.array([0,0])  # 1/MeV

    def __init__(self, energy):
        self.energy  # MeV
        maxMomentum = math.sqrt(energy ** 2 - self.mass ** 2)
        self.momentum = np.array([maxMomentum,0])

    def evolution(self,dt):
        pMod = math.sqrt(np.dot(self.momentum,self.momentum))
        vMod = p2v(pMod)
        v = vMod*self.momentum/pMod
        for i in [0,1]:
            self.position[i] = v[i] * dt


class Proton:
    mass = 938.272  # MeV
    position = np.array([0,0])

    def __init__(self, energy):
        self.energy  # MeV
        maxMomentum = math.sqrt(energy ** 2 - self.mass ** 2)
        self.momentum = np.array([maxMomentum, 0])

    def evolution(self,dt):
        pMod = math.sqrt(np.dot(self.momentum,self.momentum))
        vMod = p2v(pMod)
        v = vMod*self.momentum/pMod
        for i in [0,1]:
            self.position[i] = v[i] * dt

#  Defining Utils for execution
def Vect2D(Energy):
    Rad = np.random.normal(Energy,0.1*Energy)
    theta = np.random.normal(0,0.01)
    x = Rad * math.cos(theta)
    y = Rad * math.sin(theta)
    return np.array([[x, y]])


def interaction(Energy, momentum,dEnergy):
    newEnergy = Energy-dEnergy
    newMomentum = - momentum
    return newEnergy, newMomentum


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
            nEvents = int(input("Nombre d'events = "))
            energy = float(input("Energia del feix = "))
            break
        except:
            input("Ha ocorregut un error, polse una tecla per continuar.")
            continue
    return nEvents, energy


Nevents, Energy = 1, 100




axes = plt.gca()
axes.axis('auto')

for i in range(Nevents):
    print('Calculating particle',i+1)
    particle(np.random.normal(Energy,1))

plt.show()

