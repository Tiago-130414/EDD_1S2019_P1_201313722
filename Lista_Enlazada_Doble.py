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
        self.tamanio = -1
        self.cabezaListaD = None

    def estaVacia(self):
        return True if self.cabezaListaD is None else False    

    def agregarPrincipio(self, posicionX, posicionY):
        #agrega al principio de la lista
        nuevo_nodo = NodoD(posicionX,posicionY)
        nuevo_nodo.siguiente = self.cabezaListaD
        nuevo_nodo.anterior = None

        if self.cabezaListaD is not None:
            self.cabezaListaD.anterior = nuevo_nodo

        self.cabezaListaD = nuevo_nodo    
        self.tamanio +=1
        #print("agregado con exito al inicio")

    def agregarFinal(self,posicionX,posicionY):
        #agrega al final de la lista
        nuevo_nodo = NodoD(posicionX,posicionY) 
        last = self.cabezaListaD
        nuevo_nodo.siguiente = None

        if self.cabezaListaD is None:
            nuevo_nodo.anterior = None
            self.cabezaListaD = nuevo_nodo
            self.tamanio +=1
            return

        while (last.siguiente is not None):
            last = last.siguiente

        last.siguiente = nuevo_nodo
        nuevo_nodo.anterior = last        
        self.tamanio +=1    
        #print("agregado con exito al final")

    def mostrar (self, nodo):
        while (nodo is not None):
            print(str(nodo.posX) + ',' + str(nodo.posY))
            last = nodo
            nodo = nodo.siguiente
           
        print("De regreso: ")
        while(last is not None):
            print(str(last.posX) + ',' + str(last.posY))
            last = last.anterior
            
    def eliminarPrincipio(self):
        if(self.cabezaListaD is not None):
            primero = self.cabezaListaD
            primero = primero.siguiente
            primero.anterior = None
            self.cabezaListaD = primero

    def eliminarFinal(self):
        aux = self.cabezaListaD
        while(aux is not None):
            if(aux.siguiente is None):
                last = aux.anterior
                aux.anterior = None
                last.siguiente = None
                self.tamanio-=1
                return
            aux = aux.siguiente   

    def listG(self,node):
        cad =""
        cad+= self.agregarPNull()
        while(node is not None):
           cad += "Nodo"+str(node.posX) +"C"+str(node.posY)+ "[label=\"{"+" |"+str(node.posX)+","+str(node.posY)+"| "+"}\"style = filled, fillcolor = \"orange:red\"];"+"\n" 
           node = node.siguiente
        cad+= self.agregarUNull()   
        return cad

    def listarElementosLD(self,node):
        t = ""
        t+=self.agregarPrimerNull(self.cabezaListaD)
        while(node is not None):
           if(node.siguiente!=None):
                t += "Nodo"+str(node.posX) +"C"+str(node.posY)+"->"+"Nodo"+str(node.siguiente.posX) +"C"+str(node.siguiente.posY)+";\n" 
                t += "Nodo"+str(node.siguiente.posX) +"C"+str(node.siguiente.posY)+"->"+"Nodo"+str(node.posX) +"C"+str(node.posY)+";\n"      
           node = node.siguiente
        t+=self.agregarUltimoNull(self.cabezaListaD)
        return t

    def agregarPrimerNull(self,nodo):
        cad=""
        while(nodo is not None):
            if(nodo==self.cabezaListaD):
                cad = "NodoPN->"+ "Nodo"+str(nodo.posX) +"C"+str(nodo.posY)+"[dir=back];\n"
                break
            nodo = nodo.siguiente    
        return cad

    def agregarPNull(self):
        cad = "NodoPN"+"[label=\""+"NULL"+"\"style = filled, fillcolor = \"orange:red\"];"+"\n"
        return cad   

    def agregarUNull(self):
        cad = "NodoUN"+"[label=\""+"NULL"+"\"style = filled, fillcolor = \"orange:red\"];"+"\n"
        return cad   

    def agregarUltimoNull(self,nodo):
        cad=""
        while(nodo is not None):
            if (nodo.siguiente==None):
                cad = "Nodo"+str(nodo.posX) +"C"+str(nodo.posY)+"->NodoUN;\n"
            nodo = nodo.siguiente
                       
        return cad        

    def graficarListaDoble(self):

        if(self.estaVacia()):
            return
        else:
            listado = self.listarElementosLD(self.cabezaListaD)
            ruta_Grafica_LD = "C:/Users/santi/OneDrive/Desktop/EDD_1S2019_P1_201313722/graficaLD.dot"
            archivo = open(ruta_Grafica_LD,'w')
            archivo.writelines("digraph{\n")
            archivo.write("rankdir=LR;\n")
            archivo.write("labelloc=\"t\";\n")
            archivo.write("subgraph cluster_0{\n")
            archivo.write("style=filled;\n")
            archivo.write("color = lightgrey;\n")  
            archivo.write("node[shape=record];\n")
            archivo.write(self.listG(self.cabezaListaD))    
            archivo.write(listado)
            archivo.write("label = \"Lista Doblemente Enlazada\";\n")
            archivo.write("}\n")   
            archivo.write("}\n")   
            archivo.close() 
            os.system("dot C:\\Users\\santi\\OneDrive\\Desktop\\EDD_1S2019_P1_201313722\\graficaLD.dot -o C:\\Users\\santi\\OneDrive\\Desktop\\EDD_1S2019_P1_201313722\\graficaLD.png -Tpng -Gcharset=utf8")
            os.system("C:\\Users\\santi\\OneDrive\\Desktop\\EDD_1S2019_P1_201313722\\graficaLD.png")   

    def tamano(self):
        return self.tamanio        

    def limpiarLista(self):
        self.cabezaListaD = None    

    def ultimoNodoX(self):
        posX=0
        aux = self.cabezaListaD
        while(aux is not None):
            if(aux.siguiente is None):
                posX = aux.posX
                return posX
            aux = aux.siguiente    

    def ultimoNodoY(self):
        posY=0
        aux = self.cabezaListaD
        while(aux is not None):
            if(aux.siguiente is None):
                posY = aux.posY
                return posY
            aux = aux.siguiente        