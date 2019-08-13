import curses
from curses import KEY_RIGHT,KEY_LEFT,KEY_UP,KEY_DOWN
from play import juego
from Scoreboard import mostrarInfo
from UserSelection import seleccionar
from Reports import reportar
from BulkLoading import cargar
from play import funcionalidad
#estructuras
from cola import Cola
from Lista_Circular_Doble import Lista_Circular
from leerArchivo import lector
from Lista_Enlazada_Doble import ListaDoble
from pila import Pila
usuario = ""
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
window.keypad(True)
curses.noecho()
curses.curs_set(0)
menu(window)
#objetos para acceder a listas y a funcionalidad
fila = Cola()
listaCircular = Lista_Circular()
l = lector()
listaD = ListaDoble()
comida = ListaDoble()
comidaMala = ListaDoble()
pil = Pila()
#casos del menu
opcion =-1
while(opcion == -1):
    opcion = window.getch()
    if(opcion==49):
        #play
        usuario = juego(window,str(usuario))
        usuario = usuario.replace(' ','')
        usuario = usuario.replace('\n','')
        funcionalidad(window,usuario,listaD,comida,comidaMala,pil)
        menu(window)
        if(listaCircular.estaVacia()):
            listaCircular.agregarFinal(usuario)
        elif(listaCircular.existe(usuario)==False):
            listaCircular.agregarFinal(usuario)
        else:         
            opcion=-1  
        opcion = -1
    elif(opcion==50):
        #scoreboard
        mostrarInfo(window,fila.ultimo)
        menu(window)
        opcion = -1
    elif(opcion==51):
        #seleccion usuario
        if(listaCircular.estaVacia()):
            opcion = -1
        else:
            usuario = seleccionar(window,listaCircular)
            menu(window)
            print(usuario)
            opcion = -1    
    elif(opcion==52):
        #reportes
        reportar(window,fila,listaCircular,listaD,pil)
        menu(window)
        opcion = -1
    elif(opcion==53):
        #carga masiva
        nomAr=cargar(window)
        nomAr=nomAr+".csv"
        nomAr = nomAr.replace('\n','')
        nomAr = nomAr.replace(' ','')
        l.leer(nomAr,listaCircular)
        menu(window)
        opcion = -1
    elif(opcion==54):
        #salida
        pass    
    else:
        opcion = -1

curses.endwin()