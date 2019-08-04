import os
import sys
from Lista_Enlazada_Doble import ListaDoble

lista = ListaDoble()
lista.agregarFinal(10,2)
lista.agregarFinal(10,3)
lista.agregarPrincipio(10,1)
lista.agregarPrincipio(10,0)
lista.mostrar(lista.cabezaListaD)
lista.graficarListaDoble()
os.system("dot C:\\Users\\santi\\OneDrive\\Desktop\\EDD_1S2019_P1_201313722\\graficaLD.dot -o C:\\Users\\santi\\OneDrive\\Desktop\\EDD_1S2019_P1_201313722\\graficaLD.png -Tpng -Gcharset=utf8")