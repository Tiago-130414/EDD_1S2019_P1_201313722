import sys
import os
class NodoD:
  def __init__(self, posX,posY):
    #nodo de tipo lista doble  
    self.posX = posX
    self.posY = posY
    self.siguiente = None
    self.anterior = None

class ListaDoble:
    #lista para desplazarse en el tablero de snake
    def __init__(self):
        #constructor que inicializa nodo cabeza
        self.cabezaListaD = None

    def agregarPrincipio(self, posicionX, posicionY):
        #agrega al principio de la lista
        nuevo_nodo = NodoD(posicionX,posicionY)
        nuevo_nodo.siguiente = self.cabezaListaD
        nuevo_nodo.anterior = None

        if self.cabezaListaD is not None:
            self.cabezaListaD.anterior = nuevo_nodo

        self.cabezaListaD = nuevo_nodo    

    def agregarFinal(self,posicionX,posicionY):
        #agrega al final de la lista
        nuevo_nodo = NodoD(posicionX,posicionY)
        nuevo_nodo.siguiente = None
        last = self.cabezaListaD

        if self.cabezaListaD is None:
            nuevo_nodo.anterior = None
            self.cabezaListaD = nuevo_nodo
            return

        while (last.siguiente is not None):
            last = last.siguiente

        last.siguiente = nuevo_nodo
        nuevo_nodo.anterior = last        
        print("prueba")

    