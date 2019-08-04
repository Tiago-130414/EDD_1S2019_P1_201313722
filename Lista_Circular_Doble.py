class nodoLCD:
    def __init__(self,usuario):
        self.usuario=usuario
        self.siguiente = None
        self.anterior  = None

class Lista_Circular:
    def __init__(self):
        self.cabezaLCD=None

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

        last.siguiente = nuevo_nodo
        nuevo_nodo.anterior = last
        nuevo_nodo.siguiente = self.cabezaLCD       
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
                cad+= "Nodo"+str(nodo.usuario)+"[label=\""+str(nodo.usuario)+"\"style = filled, fillcolor = \"red:blue\"];"+"\n"
                nodo = nodo.siguiente
                if(nodo==self.cabezaLCD):
                    break
        return cad     

    def listadoUsr(self,nodo):
        cad =""
        if(self.cabezaLCD is not None):
             while(True):
                cad+= "Nodo"+str(nodo.usuario)+"->"+"Nodo"+str(nodo.siguiente.usuario)+"\n"
                cad+= "Nodo"+str(nodo.siguiente.usuario)+"->"+"Nodo"+str(nodo.usuario)+"\n"
                nodo = nodo.siguiente
                if(nodo==self.cabezaLCD):
                    break
        return cad          

    def graficarLCD(self):
        listado = self.listadoUsr(self.cabezaLCD)
        ruta_Grafica_LD = "C:/Users/santi/OneDrive/Desktop/EDD_1S2019_P1_201313722/graficaLCD.dot"
        archivo = open(ruta_Grafica_LD,'w')
        archivo.writelines("digraph{\n")
        archivo.write("rankdir=LR;\n")
        #archivo.write("labelloc=\"t\";\n")
        archivo.write("subgraph cluster_0{")
        archivo.write("style=filled;")
        archivo.write("color = lightgrey;")  
        archivo.write("node[shape=rectangle]\n")
        archivo.write(self.listarNodo(self.cabezaLCD))    
        archivo.write(listado)
        archivo.write("label = \"Lista Circular Doblemente Enlazada\";\n")
        archivo.write("}\n")   
        archivo.write("}\n")   
        archivo.close()          