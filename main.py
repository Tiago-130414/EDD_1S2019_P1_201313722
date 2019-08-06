import os
import sys
from Lista_Enlazada_Doble import ListaDoble
from Lista_Circular_Doble import Lista_Circular
from pila import Pila
from cola import Cola
"""lista = ListaDoble()
lista.agregarFinal(10,2)
lista.agregarFinal(10,3)
lista.agregarPrincipio(10,1)
lista.agregarPrincipio(10,0)
lista.agregarFinal(10,4)
lista.agregarFinal(10,5)
lista.agregarFinal(10,6)
lista.mostrar(lista.cabezaListaD)
lista.graficarListaDoble()
os.system("dot C:\\Users\\santi\\OneDrive\\Desktop\\EDD_1S2019_P1_201313722\\graficaLD.dot -o C:\\Users\\santi\\OneDrive\\Desktop\\EDD_1S2019_P1_201313722\\graficaLD.png -Tpng -Gcharset=utf8")

listaC = Lista_Circular()
listaC.agregarFinal("hola")
listaC.agregarFinal("hola1")
listaC.agregarFinal("hola2")
listaC.agregarFinal("hola3")
listaC.agregarFinal("hola4")
listaC.agregarFinal("hola5")
listaC.mostrarLCD(listaC.cabezaLCD)
listaC.graficarLCD()
os.system("dot C:\\Users\\santi\\OneDrive\\Desktop\\EDD_1S2019_P1_201313722\\graficaLCD.dot -o C:\\Users\\santi\\OneDrive\\Desktop\\EDD_1S2019_P1_201313722\\graficaLCD.png -Tpng -Gcharset=utf8")"""

"""objP = Pila()
objP.apilar(10,2)
objP.apilar(11,3)
objP.apilar(12,4)
objP.apilar(13,5)
objP.graficarPila()
os.system("dot C:\\Users\\santi\\OneDrive\\Desktop\\EDD_1S2019_P1_201313722\\graficaPila.dot -o C:\\Users\\santi\\OneDrive\\Desktop\\EDD_1S2019_P1_201313722\\graficaPila.png -Tpng -Gcharset=utf8")
"""
fila = Cola()
fila.encolar("juan",15)
fila.encolar("mario",20)
fila.encolar("jennifer",5)
fila.mostrar()
fila.desencolar()
fila.desencolar()
fila.desencolar()
fila.encolar("funciono",100)
fila.mostrar()
fila.graficar()
os.system("dot C:\\Users\\santi\\OneDrive\\Desktop\\EDD_1S2019_P1_201313722\\graficaCola.dot -o C:\\Users\\santi\\OneDrive\\Desktop\\EDD_1S2019_P1_201313722\\graficaCola.png -Tpng -Gcharset=utf8")
os.system("C:\\Users\\santi\\OneDrive\\Desktop\\EDD_1S2019_P1_201313722\\graficaCola.png")
