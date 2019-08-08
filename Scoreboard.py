import curses
import time

def mostrarInfo(window):
    titulo(window,'S c o r e    B o a r d')
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK) 
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

"""stdscr = curses.initscr()
curses.start_color()
window = curses.newwin(20,60,0,0)
curses.noecho()
curses.curs_set(0)
mostrarInfo(window)"""        