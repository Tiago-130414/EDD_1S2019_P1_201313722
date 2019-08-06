class nodoCola:
    def __init__(self,usuario,puntuacion):
        self.tamanio = 0
        self.usuario = usuario
        self.puntuacion = puntuacion
        self.siguiente = None
class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.contar = 0

    def estaVacia(self):
        return True if self.ultimo is None else False

    def encolar(self,usuario,puntuacion):
        nuevo_nodo = nodoCola(usuario,puntuacion)
        if (self.estaVacia()):
            self.ultimo= nuevo_nodo
            self.primero = self.ultimo
            print("primer nodo agregado")
            return
        self.primero.siguiente = nuevo_nodo
        self.primero = nuevo_nodo
        print("nodo agregado")

    def desencolar(self):
        if(self.estaVacia()):
            print("cola se encuentra vacia")
        elif(self.ultimo==self.primero):  
            self.ultimo=None
            self.primero = None  
            print("se elimino unico nodo")
        else:
            aux = self.ultimo
            while(aux!=self.primero):
                if(aux.siguiente==self.primero):
                    aux.siguiente=None
                    self.primero = aux
                    print("eliminado primero")
                    return
                aux = aux.siguiente

    def mostrar(self):
        aux = self.ultimo
        if(aux is None):
            print("Cola Vacia") 
        else:    
            while(aux!=None):
             print("usuario: "+str(aux.usuario)+" Puntuacion: "+str(aux.puntuacion))
             aux = aux.siguiente

    def listadoScore(self):
        aux = self.ultimo
        cad=""
        while(aux!=None):
            cad += "Nodo" + str(aux.usuario) + "[label=\""+str(aux.usuario)+","+str(aux.puntuacion)+"\"style = filled, fillcolor = \"purple:blue\"];"+"\n" 
            aux = aux.siguiente
        cad += "NodoNULL"+ "[label=\""+"NULL"+"\"style = filled, fillcolor = \"purple:blue\"];"+"\n"         
        return cad

    def apuntar(self):
        temp = self.ultimo
        cad=""
        while(temp != None):
            if(temp.siguiente!=None):
                cad +="Nodo" + str(temp.usuario)+"->Nodo"+str(temp.siguiente.usuario)+";\n"
            temp = temp.siguiente    
        cad += self.agregarUNull()
        return cad    

    def agregarUNull(self):
        t = self.ultimo
        cad=""
        while(t!=None):
            if(t.siguiente==None):
                cad = "Nodo"+str(t.usuario)+"->NodoNULL;\n"
            t = t.siguiente
        return cad        
    
    def graficar(self):
        #listado = self.listarElementosLD(self.cabezaListaD)
        ruta_Grafica_LD = "C:/Users/santi/OneDrive/Desktop/EDD_1S2019_P1_201313722/graficaCola.dot"
        archivo = open(ruta_Grafica_LD,'w')
        archivo.writelines("digraph D{\n")
        archivo.write("rankdir=LR;\n")
        archivo.write("labelloc=\"t\";\n")
        archivo.write("subgraph cluster_0{\n")
        archivo.write("style=filled;\n")
        archivo.write("color = lightgrey;\n")  
        archivo.write("node[shape=rectangle];\n")
        archivo.write(self.listadoScore())
        archivo.write(self.apuntar())   
        archivo.write("label = \"Cola\";\n")
        archivo.write("}\n")   
        archivo.write("}\n")   
        archivo.close()   