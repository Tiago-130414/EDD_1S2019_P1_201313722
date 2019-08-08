import curses
import time
from curses import KEY_RIGHT,KEY_LEFT,KEY_UP,KEY_DOWN
from Scoreboard import mostrarInfo
from UserSelection import seleccionar
from Reports import reportar
from BulkLoading import cargar

def menu(window):
    titulo(window,'M    E   N   U')
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK) 
    window.addstr(7,21,'1.-  Play',curses.color_pair(2))
    window.addstr(8,21,'2.-  Scoreboard',curses.color_pair(2))
    window.addstr(9,21,'3.-  User Selection',curses.color_pair(2))
    window.addstr(10,21,'4.-  Reports',curses.color_pair(2))
    window.addstr(11,21,'5.-  Bulk Loading',curses.color_pair(2))
    window.addstr(12,21,'6.-  Salir',curses.color_pair(2))
    window.timeout(-1)
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

stdscr = curses.initscr()
curses.start_color()
window = curses.newwin(20,60,0,0)
curses.noecho()
curses.curs_set(0)
menu(window)

opcion =-1
while(opcion == -1):
    opcion = window.getch()
    if(opcion==49):
        menu(window)
        opcion = -1
    elif(opcion==50):
        mostrarInfo(window)
        menu(window)
        opcion = -1
    elif(opcion==51):
        seleccionar(window)
        menu(window)
        opcion = -1
    elif(opcion==52):
        reportar(window)
        menu(window)
        opcion = -1
    elif(opcion==53):
        cargar(window)
        menu(window)
        opcion = -1
    elif(opcion==54):
        pass    
    else:
        opcion = -1

curses.endwin()