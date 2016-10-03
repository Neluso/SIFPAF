import randomVector
import matplotlib.pyplot as plt


#  Defining Beam
while True:
    break
    try:
        Intensity = float(input("Intensitat del feix (partícules/s) = "))
        Energy = int(input("Energia del feix (Mev) = "))
        break
    except:
        input("Ha ocorregut un error, polse una tecla per continuar.")
        continue

Nevents = 100  #  -> Intensity
Rad = 10.  # -> Energy


#  Create events
def generateEvents(Nev):
    for i in range(Nev):
        vect = randomVector.Vect2D(Rad)
        plt.arrow(0, 0, vect[0], vect[1],length_includes_head=True,width=0.001*Rad)
        axes = plt.gca()
        axes.set_xlim([0,Rad])
        axes.set_ylim([-Rad,Rad])

generateEvents(Nevents)
plt.show()
