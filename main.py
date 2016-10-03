import randomVector
import matplotlib.pyplot as plt


#  Defining Beam
while True:
    try:
        Intensity = float(input("Intensitat del feix (partícules/s) = "))
        Energy = int(input("Energia del feix (Mev) = "))
        break
    except:
        input("Ha ocorregut un error, polse una tecla per continuar.")
        continue

Nevents = 1000  #  -> Intensity


#  Create events
def generateEvents(Nev, Ener):
    for i in range(Nev):
        vect = randomVector.Vect2D(Ener)
        plt.arrow(0, 0, vect[0], vect[1],length_includes_head=True,width=0.0008*Ener)


generateEvents(Nevents,Energy)

axes = plt.gca()
axes.set_xlim([0,Energy])
axes.set_ylim([-Energy,Energy])
plt.show()
