import curses
import time
from curses import KEY_RIGHT,KEY_LEFT,KEY_UP,KEY_DOWN,KEY_ENTER
from curses.textpad import Textbox, rectangle
from random import randint
def juego(window,usr):
    if(len(usr) is 0):  
        usr = noExisteUSR(window)
        print("hola" + str(usr))
        return usr
    else:
        print(str(usr))
        return usr

def funcionalidad(window,Usr,listaDoble=object,listaComida = object,comidaMala=object,pil = object):
    valP = 0
    pts = "Score:"+str(valP)
    pts = pts.replace(' ','')
    pts = pts.replace('\n','')
    pts = pts.replace('\t','')
    usr = "Usr:"+Usr
    usr = usr.replace(' ','')
    usr = usr.replace('\n','')
    usr = usr.replace('\t','')
    tit ="Snake Reload"       
    titulo(window,tit,usr,pts)
    salida = KEY_RIGHT
    posX=5
    posY=5
    snake="#"
    curses.init_pair(6, curses.COLOR_GREEN, curses.COLOR_BLACK)
    crearSnakeInicial(posX,posY,listaDoble)
    insertarComida(listaComida)
    imprimeAsteriscos(window,snake,listaDoble)
    mostrarComida(window,listaComida)
    insertarComida(comidaMala)
    mostrarComidaM(window,comidaMala)
    #salida = window.getch()
    while(salida!=27):  
        window.timeout(200)
        mov = window.getch()
        if(mov is not -1):
           salida = mov      
        if(salida==KEY_RIGHT):
                ultX = listaDoble.ultimoNodoX()
                ultY = listaDoble.ultimoNodoY() 
                posCX = retornarPosXComida(listaComida)
                posCY = retornarPosYComida(listaComida) 
                posMX = retornarPosXComida(comidaMala)
                posMY = retornarPosYComida(comidaMala)
                #print("ult posx:" +str(ultX))  
                posX = posX+1
                if(posX >= 59):
                    posX = 1
                    listaDoble.agregarPrincipio(posX,posY)
                    if(posX==posCX and posY==posCY):
                        imprimeAsteriscos(window,snake,listaDoble)  
                        window.addstr(ultY,ultX," ")
                        print("comi")
                        valP+=1
                        pts = "Score:"+str(valP)
                        pts = pts.replace(' ','')
                        pts = pts.replace('\n','')
                        pts = pts.replace('\t','')
                        window.addstr(0,4,pts,curses.color_pair(6))
                        pil.apilar(posCX,posCY)
                        eliminarComida(listaComida)
                        insertarComida(listaComida)
                        mostrarComida(window,listaComida)
                    elif(posX==posMX and posY==posMY):
                        ultX = listaDoble.ultimoNodoX()
                        ultY = listaDoble.ultimoNodoY()
                        window.addstr(ultY,ultX," ")
                        listaDoble.eliminarFinal()
                        imprimeAsteriscos(window,snake,listaDoble)  
                        ultX = listaDoble.ultimoNodoX()
                        ultY = listaDoble.ultimoNodoY()
                        window.addstr(ultY,ultX," ")
                        listaDoble.eliminarFinal()
                        print("comi mal")
                        valP-=1
                        pts = "Score:"+str(valP)
                        pts = pts.replace(' ','')
                        pts = pts.replace('\n','')
                        pts = pts.replace('\t','')
                        window.addstr(0,4,pts,curses.color_pair(6))
                        pil. desapilar()
                        eliminarComida(comidaMala)
                        insertarComida(comidaMala)
                        mostrarComidaM(window,comidaMala)
                    else:        
                        imprimeAsteriscos(window,snake,listaDoble)  
                        window.addstr(ultY,ultX," ")
                        listaDoble.eliminarFinal()
                else:
                    listaDoble.agregarPrincipio(posX,posY)    
                    if(posX==posCX and posY==posCY):
                        imprimeAsteriscos(window,snake,listaDoble)  
                        window.addstr(ultY,ultX," ")
                        print("comi")
                        valP+=1
                        pts = "Score:"+str(valP)
                        pts = pts.replace(' ','')
                        pts = pts.replace('\n','')
                        pts = pts.replace('\t','')
                        window.addstr(0,4,pts,curses.color_pair(6))
                        pil.apilar(posCX,posCY)
                        eliminarComida(listaComida)
                        insertarComida(listaComida)
                        mostrarComida(window,listaComida)
                    elif(posX==posMX and posY==posMY):
                        ultX = listaDoble.ultimoNodoX()
                        ultY = listaDoble.ultimoNodoY()
                        window.addstr(ultY,ultX," ")
                        listaDoble.eliminarFinal()
                        imprimeAsteriscos(window,snake,listaDoble)  
                        ultX = listaDoble.ultimoNodoX()
                        ultY = listaDoble.ultimoNodoY()
                        window.addstr(ultY,ultX," ")
                        listaDoble.eliminarFinal()
                        print("comi Mal")
                        valP-=1
                        pts = "Score:"+str(valP)
                        pts = pts.replace(' ','')
                        pts = pts.replace('\n','')
                        pts = pts.replace('\t','')
                        window.addstr(0,4,pts,curses.color_pair(6))
                        pil. desapilar()
                        eliminarComida(comidaMala)
                        insertarComida(comidaMala)
                        mostrarComidaM(window,comidaMala)    
                    else:
                        imprimeAsteriscos(window,snake,listaDoble)  
                        window.addstr(ultY,ultX," ")
                        listaDoble.eliminarFinal()    
        elif(salida==KEY_LEFT):
                ultX = listaDoble.ultimoNodoX()
                ultY = listaDoble.ultimoNodoY() 
                posCX = retornarPosXComida(listaComida)
                posCY = retornarPosYComida(listaComida) 
                posMX = retornarPosXComida(comidaMala)
                posMY = retornarPosYComida(comidaMala)
                #print("ult posx:" +str(ultX))  
                posX = posX-1 
                if(posX<=1):
                    posX = 58
                    listaDoble.agregarPrincipio(posX,posY)
                    if(posX==posCX and posY==posCY):
                        imprimeAsteriscos(window,snake,listaDoble)  
                        window.addstr(ultY,ultX," ")
                        print("comi")
                        valP+=1
                        pts = "Score:"+str(valP)
                        pts = pts.replace(' ','')
                        pts = pts.replace('\n','')
                        pts = pts.replace('\t','')
                        window.addstr(0,4,pts,curses.color_pair(6))
                        pil.apilar(posCX,posCY)
                        eliminarComida(listaComida)
                        insertarComida(listaComida)
                        mostrarComida(window,listaComida)
                    elif(posX==posMX and posY==posMY):
                        ultX = listaDoble.ultimoNodoX()
                        ultY = listaDoble.ultimoNodoY()
                        window.addstr(ultY,ultX," ")
                        listaDoble.eliminarFinal()
                        imprimeAsteriscos(window,snake,listaDoble)  
                        ultX = listaDoble.ultimoNodoX()
                        ultY = listaDoble.ultimoNodoY()
                        window.addstr(ultY,ultX," ")
                        listaDoble.eliminarFinal()
                        print("comi mal")
                        valP-=1
                        pts = "Score:"+str(valP)
                        pts = pts.replace(' ','')
                        pts = pts.replace('\n','')
                        pts = pts.replace('\t','')
                        window.addstr(0,4,pts,curses.color_pair(6))
                        pil. desapilar()
                        eliminarComida(comidaMala)
                        insertarComida(comidaMala)
                        mostrarComidaM(window,comidaMala)    
                    else:
                        imprimeAsteriscos(window,snake,listaDoble)  
                        window.addstr(ultY,ultX," ")    
                        listaDoble.eliminarFinal()
                else:
                    listaDoble.agregarPrincipio(posX,posY)
                    if(posX==posCX and posY==posCY):
                        imprimeAsteriscos(window,snake,listaDoble)  
                        window.addstr(ultY,ultX," ")
                        print("comi")
                        valP+=1
                        pts = "Score:"+str(valP)
                        pts = pts.replace(' ','')
                        pts = pts.replace('\n','')
                        pts = pts.replace('\t','')
                        window.addstr(0,4,pts,curses.color_pair(6))
                        pil.apilar(posCX,posCY)
                        eliminarComida(listaComida)
                        insertarComida(listaComida)
                        mostrarComida(window,listaComida)
                    elif(posX==posMX and posY==posMY):
                        ultX = listaDoble.ultimoNodoX()
                        ultY = listaDoble.ultimoNodoY()
                        window.addstr(ultY,ultX," ")
                        listaDoble.eliminarFinal()
                        imprimeAsteriscos(window,snake,listaDoble)  
                        ultX = listaDoble.ultimoNodoX()
                        ultY = listaDoble.ultimoNodoY()
                        window.addstr(ultY,ultX," ")
                        listaDoble.eliminarFinal()
                        print("comi mal")
                        valP-=1
                        pts = "Score:"+str(valP)
                        pts = pts.replace(' ','')
                        pts = pts.replace('\n','')
                        pts = pts.replace('\t','')
                        window.addstr(0,4,pts,curses.color_pair(6))
                        pil. desapilar()
                        eliminarComida(comidaMala)
                        insertarComida(comidaMala)
                        mostrarComidaM(window,comidaMala)    
                    else:
                        imprimeAsteriscos(window,snake,listaDoble)  
                        window.addstr(ultY,ultX," ")    
                        listaDoble.eliminarFinal()        
        elif(salida==KEY_UP):
                ultX = listaDoble.ultimoNodoX()
                ultY = listaDoble.ultimoNodoY() 
                posCX = retornarPosXComida(listaComida)
                posCY = retornarPosYComida(listaComida) 
                posMX = retornarPosXComida(comidaMala)
                posMY = retornarPosYComida(comidaMala)
                #print("ult posy:" +str(ultY))  
                posY = posY-1
                if(posY<=1):
                   posY=18
                   listaDoble.agregarPrincipio(posX,posY)
                   if(posX==posCX and posY==posCY):
                        imprimeAsteriscos(window,snake,listaDoble)  
                        window.addstr(ultY,ultX," ")
                        print("comi")
                        valP+=1
                        pts = "Score:"+str(valP)
                        pts = pts.replace(' ','')
                        pts = pts.replace('\n','')
                        pts = pts.replace('\t','')
                        window.addstr(0,4,pts,curses.color_pair(6))
                        pil.apilar(posCX,posCY)
                        eliminarComida(listaComida)
                        insertarComida(listaComida)
                        mostrarComida(window,listaComida)
                   elif(posX==posMX and posY==posMY):
                        ultX = listaDoble.ultimoNodoX()
                        ultY = listaDoble.ultimoNodoY()
                        window.addstr(ultY,ultX," ")
                        listaDoble.eliminarFinal()
                        imprimeAsteriscos(window,snake,listaDoble)  
                        ultX = listaDoble.ultimoNodoX()
                        ultY = listaDoble.ultimoNodoY()
                        window.addstr(ultY,ultX," ")
                        listaDoble.eliminarFinal()
                        print("comi mal")
                        valP-=1
                        pts = "Score:"+str(valP)
                        pts = pts.replace(' ','')
                        pts = pts.replace('\n','')
                        pts = pts.replace('\t','')
                        window.addstr(0,4,pts,curses.color_pair(6))
                        pil. desapilar()
                        eliminarComida(comidaMala)
                        insertarComida(comidaMala)
                        mostrarComidaM(window,comidaMala)     
                   else:
                        imprimeAsteriscos(window,snake,listaDoble)  
                        window.addstr(ultY,ultX," ")    
                        listaDoble.eliminarFinal()
                else:
                   listaDoble.agregarPrincipio(posX,posY)
                   if(posX==posCX and posY==posCY):
                        imprimeAsteriscos(window,snake,listaDoble)  
                        window.addstr(ultY,ultX," ")
                        print("comi")
                        valP+=1
                        pts = "Score:"+str(valP)
                        pts = pts.replace(' ','')
                        pts = pts.replace('\n','')
                        pts = pts.replace('\t','')
                        window.addstr(0,4,pts,curses.color_pair(6))
                        pil.apilar(posCX,posCY)
                        eliminarComida(listaComida)
                        insertarComida(listaComida)
                        mostrarComida(window,listaComida)
                   elif(posX==posMX and posY==posMY):
                        ultX = listaDoble.ultimoNodoX()
                        ultY = listaDoble.ultimoNodoY()
                        window.addstr(ultY,ultX," ")
                        listaDoble.eliminarFinal()
                        imprimeAsteriscos(window,snake,listaDoble)  
                        ultX = listaDoble.ultimoNodoX()
                        ultY = listaDoble.ultimoNodoY()
                        window.addstr(ultY,ultX," ")
                        listaDoble.eliminarFinal()
                        print("comi mal")
                        valP-=1
                        pts = "Score:"+str(valP)
                        pts = pts.replace(' ','')
                        pts = pts.replace('\n','')
                        pts = pts.replace('\t','')
                        window.addstr(0,4,pts,curses.color_pair(6))
                        pil. desapilar()
                        eliminarComida(comidaMala)
                        insertarComida(comidaMala)
                        mostrarComidaM(window,comidaMala)
                   else:
                        imprimeAsteriscos(window,snake,listaDoble)  
                        window.addstr(ultY,ultX," ")    
                        listaDoble.eliminarFinal()              
        elif(salida==KEY_DOWN):
                ultX = listaDoble.ultimoNodoX()
                ultY = listaDoble.ultimoNodoY() 
                posCX = retornarPosXComida(listaComida)
                posCY = retornarPosYComida(listaComida) 
                posMX = retornarPosXComida(comidaMala)
                posMY = retornarPosYComida(comidaMala)
                #print("ult posy:" +str(ultY))  
                posY = posY+1
                if(posY>=19):
                   posY = 1     
                   listaDoble.agregarPrincipio(posX,posY)
                   if(posX==posCX and posY==posCY):
                        imprimeAsteriscos(window,snake,listaDoble)  
                        window.addstr(ultY,ultX," ")
                        print("comi")
                        valP+=1
                        pts = "Score:"+str(valP)
                        pts = pts.replace(' ','')
                        pts = pts.replace('\n','')
                        pts = pts.replace('\t','')
                        window.addstr(0,4,pts,curses.color_pair(6))
                        pil.apilar(posCX,posCY)
                        eliminarComida(listaComida)
                        insertarComida(listaComida)
                        mostrarComida(window,listaComida)
                   elif(posX==posMX and posY==posMY):
                        ultX = listaDoble.ultimoNodoX()
                        ultY = listaDoble.ultimoNodoY()
                        window.addstr(ultY,ultX," ")
                        listaDoble.eliminarFinal()
                        imprimeAsteriscos(window,snake,listaDoble)  
                        ultX = listaDoble.ultimoNodoX()
                        ultY = listaDoble.ultimoNodoY()
                        window.addstr(ultY,ultX," ")
                        listaDoble.eliminarFinal()
                        print("comi mal")
                        valP-=1
                        pts = "Score:"+str(valP)
                        pts = pts.replace(' ','')
                        pts = pts.replace('\n','')
                        pts = pts.replace('\t','')
                        window.addstr(0,4,pts,curses.color_pair(6))
                        pil. desapilar()
                        eliminarComida(comidaMala)
                        insertarComida(comidaMala)
                        mostrarComidaM(window,comidaMala)
                   else:
                        imprimeAsteriscos(window,snake,listaDoble)  
                        window.addstr(ultY,ultX," ")    
                        listaDoble.eliminarFinal()    
                else:
                   listaDoble.agregarPrincipio(posX,posY)
                   if(posX==posCX and posY==posCY):
                        imprimeAsteriscos(window,snake,listaDoble)  
                        window.addstr(ultY,ultX," ")
                        print("comi")
                        valP+=1
                        pts = "Score:"+str(valP)
                        pts = pts.replace(' ','')
                        pts = pts.replace('\n','')
                        pts = pts.replace('\t','')
                        window.addstr(0,4,pts,curses.color_pair(6))
                        pil.apilar(posCX,posCY)
                        eliminarComida(listaComida)
                        insertarComida(listaComida)
                        mostrarComida(window,listaComida)
                   elif(posX==posMX and posY==posMY):
                        ultX = listaDoble.ultimoNodoX()
                        ultY = listaDoble.ultimoNodoY()
                        window.addstr(ultY,ultX," ")
                        listaDoble.eliminarFinal()
                        imprimeAsteriscos(window,snake,listaDoble)  
                        ultX = listaDoble.ultimoNodoX()
                        ultY = listaDoble.ultimoNodoY()
                        window.addstr(ultY,ultX," ")
                        listaDoble.eliminarFinal()
                        print("comi mal")
                        valP-=1
                        pts = "Score:"+str(valP)
                        pts = pts.replace(' ','')
                        pts = pts.replace('\n','')
                        pts = pts.replace('\t','')
                        window.addstr(0,4,pts,curses.color_pair(6))
                        pil. desapilar()
                        eliminarComida(comidaMala)
                        insertarComida(comidaMala)
                        mostrarComidaM(window,comidaMala)
                   else:
                        imprimeAsteriscos(window,snake,listaDoble)  
                        window.addstr(ultY,ultX," ")    
                        listaDoble.eliminarFinal()             
                
def titulo(window,texto,usr,punteo):
    window.clear()
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK) 
    pintarVentana(window)
    centro = round((60-len(texto))/2)
    print(str(centro))
    window.addstr(0,centro,texto,curses.color_pair(3))
    window.addstr(0,centro+22,usr,curses.color_pair(3))
    window.addstr(0,centro-20,punteo,curses.color_pair(3))
    
def tituloNE(window,texto):
    window.clear()
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK) 
    pintarVentana(window)
    centro = round((60-len(texto))/2)
    window.addstr(0,centro,texto,curses.color_pair(3))    

def pintarVentana(window):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    window.attron(curses.color_pair(1))
    window.border(0)
    window.attroff(curses.color_pair(1))
    window.refresh() 

def noExisteUSR(window):
    window.clear()
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK) 
    tituloNE(window, "Ingrese usuario: (Ctrl-G para guardar)")
    #window.addstr(0, 0, "Ingrese usuario: (Ctrl-G para guardar)",curses.color_pair(3))
    window.attron(curses.color_pair(4))
    #window.border(0)
    #(ancho,largo,y,x)    
    editwin = curses.newwin(3,15, 9,25)
    #(y,x,ancho,largo)    
    rectangle(window, 7,11, 1+11+1, 1+45+1)
    window.attron(curses.color_pair(4))
    window.refresh()
    box = Textbox(editwin)
    box.edit()
    persona = box.gather()
    return persona  

def crearSnakeInicial(posY,posX,listaDoble = object):
        listaDoble.agregarFinal(posX,posY)
        posX+=1
        listaDoble.agregarFinal(posX,posY)
        posX+=1
        listaDoble.agregarFinal(posX,posY)

def imprimeAsteriscos(window,snake,listaDoble = object):
    aux = listaDoble.cabezaListaD
    while(aux is not None):
        posX = aux.posX
        posY = aux.posY
        window.addstr(posY,posX,snake)
        aux = aux.siguiente

def retornarPosX():
        posX = randint(2,57)
        return posX

def retornarPosY():
        posY = randint(2,17)
        return posY       

def insertarComida(listaComida=object):        
        posX = retornarPosX()
        posY = retornarPosY()
        listaComida.agregarFinal(posX,posY)
        
def mostrarComida(window,listaComida = object):
        if(listaComida.estaVacia()):
            print("vacia")
        else:
            aux = listaComida.cabezaListaD
            while(aux is not None):
                posX = aux.posX
                posY = aux.posY
                window.addstr(posY,posX,'+')
                aux = aux.siguiente             

def retornarPosXComida(listaComida = object):
        aux = listaComida.cabezaListaD
        while(aux is not None):
                if(aux.siguiente == None):
                        posX = aux.posX
                        return posX
                aux = aux.siguiente

def retornarPosYComida(listaComida = object):
        aux = listaComida.cabezaListaD
        while(aux is not None):
                if(aux.siguiente == None):
                        posY = aux.posY
                        return posY
                aux = aux.siguiente    

def eliminarComida(listaComida=object):
        listaComida.cabezaListaD = None                    

def mostrarComidaM(window,listaComida = object):
        if(listaComida.estaVacia()):
                print("vacia")
        else:
                aux = listaComida.cabezaListaD
                while(aux is not None):
                        posX = aux.posX
                        posY = aux.posY
                        window.addstr(posY,posX,'*')
                        aux = aux.siguiente   
