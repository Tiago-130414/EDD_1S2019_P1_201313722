import curses
import time

def reportar(window, fila=object):
    titulo(window,'R e p o r t s')
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK) 
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK) 
    window.addstr(7,21,'1.-  Snake Report',curses.color_pair(2))
    window.addstr(8,21,'2.-  Score Report',curses.color_pair(2))
    window.addstr(9,21,'3.-  Score Board Report',curses.color_pair(2))
    window.addstr(10,21,'4.-  User Report',curses.color_pair(2))
    window.timeout(-1)
    opcion =-1
    while(opcion == -1):
        opcion = window.getch()
        if(opcion==49):
            #Snake Report
            reportar(window)
            opcion = -1
        elif(opcion==50):
            #score Report
            reportar(window)
            opcion = -1
        elif(opcion==51):
            #score board report 
            fila.graficar()
            reportar(window)
            opcion = -1
        elif(opcion==52):
            #user report
            reportar(window)
            opcion = -1
        elif(opcion==27):
            return     
        else:
            opcion = -1
    
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
    