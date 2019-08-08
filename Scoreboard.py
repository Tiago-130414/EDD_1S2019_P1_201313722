import curses
import time

def mostrarInfo(window,cola):
    titulo(window,'S c o r e    B o a r d')
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK) 
    window.addstr(3,21,'NAME        SCORE',curses.color_pair(2)) #cabecera
    pos =5
    while(cola != None):
        window.addstr(pos,21,str(cola.usuario)+"\t\t"+str(cola.puntuacion),curses.color_pair(2))
        pos+=1  
        cola = cola.siguiente
    salida = window.getch()
    while salida!=27:
        salida = window.getch()
    
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