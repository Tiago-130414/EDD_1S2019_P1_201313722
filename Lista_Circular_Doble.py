import os
import sys
class nodoLCD:
    def __init__(self,usuario):
        self.usuario=usuario
        self.siguiente = None
        self.anterior  = None

class Lista_Circular:
    def __init__(self):
        self.cabezaLCD=None
    def estaVacia(self):
        return True if self.cabezaLCD is None else False    

    def agregarFinal(self,user):
        nuevo_nodo = nodoLCD(user)
        last = self.cabezaLCD
       # nuevo_nodo.siguiente = None

        if (self.cabezaLCD is None):
           nuevo_nodo.siguiente = nuevo_nodo
           nuevo_nodo.anterior = nuevo_nodo
           self.cabezaLCD = nuevo_nodo
           print("agregado con exito al final")
           return

        while(last.siguiente!=self.cabezaLCD):
            last = last.siguiente

        nuevo_nodo.anterior = last
        nuevo_nodo.siguiente = self.cabezaLCD
        last.siguiente = nuevo_nodo
        self.cabezaLCD.anterior = nuevo_nodo       
        print("agregado con exito al final")

    def mostrarLCD(self,node):
       if (self.cabezaLCD is not None):
           while (True):
            print(str(node.usuario))
            node = node.siguiente
            if(node==self.cabezaLCD):
                break

    def listarNodo(self,nodo):
        cad =""
        if(self.cabezaLCD is not None):
             while(True):
                cad+= "Nodo"+str(nodo.usuario)+"[label=\"{"+" |"+str(nodo.usuario)+"| }"+"\"style = filled, fillcolor = \"red:blue\"];"+"\n"
                nodo = nodo.siguiente
                if(nodo==self.cabezaLCD):
                    break
        return cad     

    def listadoUsr(self,nodo):
        cad =""
        if(self.cabezaLCD is not None):
             while(True):
                cad+= "Nodo"+str(nodo.usuario)+"->"+"Nodo"+str(nodo.siguiente.usuario)+";\n"
                cad+= "Nodo"+str(nodo.siguiente.usuario)+"->"+"Nodo"+str(nodo.usuario)+";\n"
                nodo = nodo.siguiente
                if(nodo==self.cabezaLCD):
                    break
        return cad          

    def graficarLCD(self):
        if(self.estaVacia()):
            return
        else:
            listado = self.listadoUsr(self.cabezaLCD)
            ruta_Grafica_LD = "C:/Users/santi/OneDrive/Desktop/EDD_1S2019_P1_201313722/graficaLCD.dot"
            archivo = open(ruta_Grafica_LD,'w')
            archivo.writelines("digraph{\n")
            archivo.write("rankdir=LR;\n")
            archivo.write("labelloc=\"t\";\n")
            archivo.write("subgraph cluster_0{\n")
            archivo.write("style=filled;\n")
            archivo.write("color = lightgrey;\n")  
            archivo.write("node[shape=record];\n")
            archivo.write(self.listarNodo(self.cabezaLCD))    
            archivo.write(listado)
            archivo.write("label = \"Lista Circular Doblemente Enlazada\";\n")
            archivo.write("}\n")   
            archivo.write("}\n")   
            archivo.close() 
            os.system("dot C:\\Users\\santi\\OneDrive\\Desktop\\EDD_1S2019_P1_201313722\\graficaLCD.dot -o C:\\Users\\santi\\OneDrive\\Desktop\\EDD_1S2019_P1_201313722\\graficaLCD.png -Tpng -Gcharset=utf8")
            os.system("C:\\Users\\santi\\OneDrive\\Desktop\\EDD_1S2019_P1_201313722\\graficaLCD.png")         

    def existe(self,usuario):
        last = self.cabezaLCD
        exist = False
        while(last!=self.cabezaLCD):
            if(last.usuario==usuario):
                exit = True
                print("lo encontre")
                return exist
                #break
            last = last.siguiente
            if(last.siguiente==self.cabezaLCD):
                return exist        