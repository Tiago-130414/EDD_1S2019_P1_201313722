import os
import sys
from Lista_Enlazada_Doble import ListaDoble
from Lista_Circular_Doble import Lista_Circular

lista = ListaDoble()
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
os.system("dot C:\\Users\\santi\\OneDrive\\Desktop\\EDD_1S2019_P1_201313722\\graficaLCD.dot -o C:\\Users\\santi\\OneDrive\\Desktop\\EDD_1S2019_P1_201313722\\graficaLCD.png -Tpng -Gcharset=utf8")
