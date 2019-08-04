class NodoPila:
    def __init__(self,posX,posY):
        self.posX=posX
        self.posY=posY
        self.siguiente = None
class Pila:
    def __init__(self):
        self.head = None
    
    def estaVacia(self): 
        return True if self.head is None else  False 

    def apilar(self,posx,posy):
        nuevo = NodoPila(posx,posy)
        nuevo.siguiente = self.head
        self.head = nuevo
        print("elemento apilado")
    
    def desapilar(self):
        if (self.estaVacia()): 
            print("Pila Vacia") 
            return
        self.head = self.head.siguiente 
        print("desapilado")

    def mostrarPila(self):
        aux = self.head
        while(aux!=None):
            print("coordenadas: "+str(aux.posX)+","+str(aux.posY))
            aux = aux.siguiente
        if(aux is None):
            print("Pila Vacia")    