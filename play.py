import curses
import time
from curses import KEY_RIGHT,KEY_LEFT,KEY_UP,KEY_DOWN,KEY_ENTER
from curses.textpad import Textbox, rectangle
def juego(window,usr):
    if(len(usr) is 0):  
        usr = noExisteUSR(window)
        print("hola" + str(usr))
        return usr
    else:
        print(str(usr))
        return usr

def funcionalidad(window,usr,listaDoble=object):
    usr = usr.replace(' ','')
    usr = usr.replace('\n','')
    usr = usr.replace('\t','')
    usr ="SnakeReload"+usr       
    titulo(window,usr)
    salida = KEY_RIGHT
    posX=5
    posY=5
    snake="*"
    crearSnakeInicial(posX,posY,listaDoble)
    imprimeAsteriscos(window,snake,listaDoble)
    #salida = window.getch()
    while(salida!=27):  
        window.timeout(100)
        mov = window.getch()
        if(mov is not -1):
           salida = mov
        
        if(salida==KEY_RIGHT):
                ultX = listaDoble.ultimoNodoX()
                ultY = listaDoble.ultimoNodoY() 
                print("ult posx:" +str(ultX))  
                posX = posX+1
                listaDoble.agregarPrincipio(posX,posY)
                imprimeAsteriscos(window,snake,listaDoble)  
                window.addstr(ultY,ultX," ")
                listaDoble.eliminarFinal()
        elif(salida==KEY_LEFT):
                ultX = listaDoble.ultimoNodoX()
                ultY = listaDoble.ultimoNodoY() 
                print("ult posx:" +str(ultX))  
                posX = posX-1 
                listaDoble.agregarPrincipio(posX,posY)
                imprimeAsteriscos(window,snake,listaDoble)  
                window.addstr(ultY,ultX," ")
                listaDoble.eliminarFinal()
        elif(salida==KEY_UP):
                ultX = listaDoble.ultimoNodoX()
                ultY = listaDoble.ultimoNodoY() 
                print("ult posy:" +str(ultY))  
                posY = posY-1
                listaDoble.agregarPrincipio(posX,posY)
                imprimeAsteriscos(window,snake,listaDoble)  
                window.addstr(ultY,ultX," ")
                listaDoble.eliminarFinal()
        elif(salida==KEY_DOWN):
                ultX = listaDoble.ultimoNodoX()
                ultY = listaDoble.ultimoNodoY() 
                print("ult posy:" +str(ultY))  
                posY = posY+1
                listaDoble.agregarPrincipio(posX,posY)
                imprimeAsteriscos(window,snake,listaDoble)  
                window.addstr(ultY,ultX," ")
                listaDoble.eliminarFinal()
                
        
    
def titulo(window,texto):
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
    titulo(window, "Ingrese usuario: (Ctrl-G para guardar)")
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
      

def posicionesAumentanX(posX,posY,listaDoble=object):
        pass        