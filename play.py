import curses
import time
from curses import KEY_RIGHT,KEY_LEFT,KEY_UP,KEY_DOWN,KEY_ENTER
from curses.textpad import Textbox, rectangle
def juego(window,usr,listaDoble=object):
    if(len(usr) is 0):  
        usr = noExisteUSR(window)
        print("hola" + str(usr))
        funcionalidad(window,usr)
        return usr
    else:
        print(str(usr))
        funcionalidad(window,usr,listaDoble)
        return usr

def funcionalidad(window,usr,listaDoble=object):
    usr ="SnakeReload"+usr       
    titulo(window,usr)
    salida = KEY_RIGHT
    posX=5
    posY=5
    snake="*"
    window.addstr(posY,posX,snake)
    #salida = window.getch()
    while(salida!=27):
        window.timeout(10)
        mov = window.getch()
        if(mov is not -1):
           salida = mov
        window.addstr(posY,posX,' ')
        if(salida==KEY_RIGHT):
                posX = posX+1
        elif(salida==KEY_LEFT):
                posX = posX-1 
        elif(salida==KEY_UP):
                posY = posY-1
        elif(salida==KEY_DOWN):
                posY = posY+1                 
        window.addstr(posY,posX,snake)
    
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

def crearSnakeInicial(posX,posY,listaDoble = object):
        listaDoble.agregarFinal(posX,posY)
        posX+=1
        listaDoble.agregarFinal(posX,posY)
        posX+=1
        listaDoble.agregarFinal(posX,posY)

def cantidadAsteriscos(tamanio,listaDoble = object):
        
        pass        