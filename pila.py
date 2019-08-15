import os
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
        #print("elemento apilado")
    
    def desapilar(self):
        if (self.estaVacia()): 
            print("Pila Vacia") 
            return
        self.head = self.head.siguiente 
        #print("desapilado")

    def mostrarPila(self):
        aux = self.head
        while(aux!=None):
            print("coordenadas: "+str(aux.posX)+","+str(aux.posY))
            aux = aux.siguiente
        if(aux is None):
            print("Pila Vacia")    

    def listadoPila(self):
        cad =" |\n"
        aux = self.head
        while(aux!=None):
            cad+=str(aux.posX) +","+str(aux.posY)
            if(aux.siguiente!=None):
                cad+="|\n"
            aux = aux.siguiente
        if(aux is None):
            print("Pila Vacia")
        return cad    

    def graficarPila(self):
        if(self.estaVacia()):
            return
        else:
            ruta_Grafica_LD = "C:/Users/santi/OneDrive/Desktop/EDD_1S2019_P1_201313722/graficaPila.dot"
            archivo = open(ruta_Grafica_LD,'w')
            archivo.writelines("digraph D{\n")
            archivo.write("rankdir=TB;\n")
            archivo.write("labelloc=\"t\";\n")
            archivo.write("subgraph cluster_0{\n")
            archivo.write("style=filled;\n")
            archivo.write("color = lightgrey;\n")  
            archivo.write("node[shape=record,style = filled, fillcolor = \"purple:red\"];\n")
            archivo.write("node_GP[shape = record \n")    
            archivo.write("label=\"{\n")
            archivo.write(self.listadoPila())
            archivo.write("}\"\n")
            archivo.write("];\n")    
            archivo.write("label = \"Pila\";\n")
            archivo.write("}\n")   
            archivo.write("}\n")   
            archivo.close()
            os.system("dot C:\\Users\\santi\\OneDrive\\Desktop\\EDD_1S2019_P1_201313722\\graficaPila.dot -o C:\\Users\\santi\\OneDrive\\Desktop\\EDD_1S2019_P1_201313722\\graficaPila.png -Tpng -Gcharset=utf8")
            os.system("C:\\Users\\santi\\OneDrive\\Desktop\\EDD_1S2019_P1_201313722\\graficaPila.png")          
