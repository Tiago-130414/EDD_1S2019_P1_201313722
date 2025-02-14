import curses
from curses import KEY_RIGHT,KEY_LEFT,KEY_UP,KEY_DOWN,KEY_ENTER
usuario =" "
def seleccionar(window,listaCD = object):
    txt = ""    
    titulo(window,'U s e r  S e l e c t i o n')
    aux = listaCD.cabezaLCD
    pintarUsuario(window,aux)
    while True:
        salida = window.getch()
        if(salida == KEY_LEFT):
                #izquierda
                titulo(window,'U s e r  S e l e c t i o n')
                aux = aux.anterior
                pintarUsuario(window,aux)
        if(salida == KEY_RIGHT):
                #derecha
                titulo(window,'U s e r  S e l e c t i o n')
                aux = aux.siguiente
                pintarUsuario(window,aux)          
        if(salida == 10):
                #enter
                txt = aux.usuario
                print("presione enter")
                return txt              
        if(salida == 27):
                #salida
                break
    
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

def pintarUsuario(window,nodo):
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        texto = nodo.usuario
        centro = round((60-len(texto))/2)
        window.addstr(9,23,"<--"+texto+"-->",curses.color_pair(2))
        window.refresh()        
       