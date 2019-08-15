import curses
import time
from curses import KEY_RIGHT,KEY_LEFT,KEY_UP,KEY_DOWN,KEY_ENTER
from curses.textpad import Textbox, rectangle
from random import randint
import threading
estoyPausa = False
def juego(window,usr):
    if(len(usr) is 0):  
        usr = noExisteUSR(window)
        return usr
    else:
        return usr

def funcionalidad(window,Usr,puntos,juegoN=object,listaDoble=object,listaComida = object,comidaMala=object,pil = object,fila = object):
    curses.init_pair(6, curses.COLOR_GREEN, curses.COLOR_BLACK)
    valP = puntos
    choque = False
    pts = "Score:"+str(valP)
    usr = "Usr:"+Usr
    usr = usr.replace(' ','')
    usr = usr.replace('\n','')
    usr = usr.replace('\t','')
    tit ="Snake Reload"       
    titulo(window,tit,usr,pts)
    if(juegoN.estado is True):
                salida = KEY_RIGHT
                posX=5
                posY=5
                snake="#"
                crearSnakeInicial(posX,posY,listaDoble)
                insertarComida(listaComida)
                imprimeAsteriscos(window,snake,listaDoble)
                mostrarComida(window,listaComida)
                insertarComida(comidaMala)
                mostrarComidaM(window,comidaMala)
    else:
        salida=0
        snake="#"
        posX = listaDoble.cabezaListaD.posX
        posY = listaDoble.cabezaListaD.posY
        imprimeAsteriscos(window,snake,listaDoble)
        mostrarComida(window,listaComida)
        mostrarComidaM(window,comidaMala)           
    #salida = window.getch()
    while(salida!=27): 
        pts=""    
        window.timeout(evaluarNivel(valP))
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
                    #choca y pierde
                    choque = choqueSnake(window,listaDoble,fila)
                    if(choque == True and listaDoble.tamanio>=4):
                        salida = 0
                        perder(window)
                        fila.encolar(Usr,valP)
                        #limpiarParaJuegoNuevo(listaDoble,listaComida,comidaMala,pil)
                    listaDoble.agregarPrincipio(posX,posY)
                    if(posX==posCX and posY==posCY):
                        imprimeAsteriscos(window,snake,listaDoble)  
                        window.addstr(ultY,ultX," ")
                        curses.beep( )
                        valP+=1
                        pts1=""
                        pts1 = "Score:"+str(valP)
                        print(pts1)
                        window.addstr(0,4,"        ",curses.color_pair(6))        
                        window.addstr(0,4,pts1,curses.color_pair(6))
                        pil.apilar(posCX,posCY)
                        eliminarComida(listaComida)
                        insertarComida(listaComida)
                        mostrarComida(window,listaComida)
                    elif(posX==posMX and posY==posMY):
                        if(listaDoble.tamanio>3 and valP>0):
                                ultX = listaDoble.ultimoNodoX()
                                ultY = listaDoble.ultimoNodoY()
                                window.addstr(ultY,ultX," ")
                                listaDoble.eliminarFinal()
                                imprimeAsteriscos(window,snake,listaDoble)  
                                ultX = listaDoble.ultimoNodoX()
                                ultY = listaDoble.ultimoNodoY()
                                window.addstr(ultY,ultX," ")
                                listaDoble.eliminarFinal()
                                valP-=1  
                                pts2=""
                                pts2= "Score:"+str(valP)
                                print(pts2)
                                window.addstr(0,4,"        ",curses.color_pair(6))        
                                window.addstr(0,4,pts2,curses.color_pair(6))
                                pil. desapilar()
                                eliminarComida(comidaMala)
                                insertarComida(comidaMala)
                                mostrarComidaM(window,comidaMala)
                        else:
                                imprimeAsteriscos(window,snake,listaDoble)  
                                window.addstr(ultY,ultX," ")    
                                listaDoble.eliminarFinal()   
                                eliminarComida(comidaMala)
                                insertarComida(comidaMala)
                                mostrarComidaM(window,comidaMala)
                    else:     
                        imprimeAsteriscos(window,snake,listaDoble)  
                        window.addstr(ultY,ultX," ")
                        listaDoble.eliminarFinal()
                else:
                    #choca y pierde
                    choque = choqueSnake(window,listaDoble,fila)
                    if(choque == True and listaDoble.tamanio>=4):
                        salida = 0
                        perder(window)
                        fila.encolar(Usr,valP)
                        #limpiarParaJuegoNuevo(listaDoble,listaComida,comidaMala,pil)
                    listaDoble.agregarPrincipio(posX,posY)    
                    if(posX==posCX and posY==posCY):
                        imprimeAsteriscos(window,snake,listaDoble)  
                        window.addstr(ultY,ultX," ")
                        curses.beep( )
                        valP+=1
                        pts3=""
                        pts3= "Score:"+str(valP)
                        print(pts3)
                        window.addstr(0,4,"        ",curses.color_pair(6))
                        window.addstr(0,4,pts3,curses.color_pair(6))
                        pil.apilar(posCX,posCY)
                        eliminarComida(listaComida)
                        insertarComida(listaComida)
                        mostrarComida(window,listaComida)
                    elif(posX==posMX and posY==posMY):
                        if(listaDoble.tamanio>3 and valP>0):
                                ultX = listaDoble.ultimoNodoX()
                                ultY = listaDoble.ultimoNodoY()
                                window.addstr(ultY,ultX," ")
                                listaDoble.eliminarFinal()
                                imprimeAsteriscos(window,snake,listaDoble)  
                                ultX = listaDoble.ultimoNodoX()
                                ultY = listaDoble.ultimoNodoY()
                                window.addstr(ultY,ultX," ")
                                listaDoble.eliminarFinal()
                                valP-=1   
                                pts4=""
                                pts4 = "Score:"+str(valP)
                                print(pts4)
                                window.addstr(0,4,"        ",curses.color_pair(6))
                                window.addstr(0,4,pts4,curses.color_pair(6))      
                                pil. desapilar()
                                eliminarComida(comidaMala)
                                insertarComida(comidaMala)
                                mostrarComidaM(window,comidaMala)
                        else:
                                imprimeAsteriscos(window,snake,listaDoble)  
                                window.addstr(ultY,ultX," ")    
                                listaDoble.eliminarFinal()   
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
                    #choca y pierde
                    choque = choqueSnake(window,listaDoble,fila)
                    if(choque == True and listaDoble.tamanio>=4):
                        salida = 0
                        perder(window)
                        fila.encolar(Usr,valP)
                        #limpiarParaJuegoNuevo(listaDoble,listaComida,comidaMala,pil)
                    listaDoble.agregarPrincipio(posX,posY)
                    if(posX==posCX and posY==posCY):
                        imprimeAsteriscos(window,snake,listaDoble)  
                        window.addstr(ultY,ultX," ")
                        curses.beep( )
                        valP+=1
                        print("izquierda: "+str(valP))
                        pts5=""
                        pts5 = "Score:"+str(valP)
                        window.addstr(0,4,"        ",curses.color_pair(6))
                        window.addstr(0,4,pts5,curses.color_pair(6))
                        pil.apilar(posCX,posCY)
                        eliminarComida(listaComida)
                        insertarComida(listaComida)
                        mostrarComida(window,listaComida)
                    elif(posX==posMX and posY==posMY):
                        if(listaDoble.tamanio>3 and valP>0):
                                ultX = listaDoble.ultimoNodoX()
                                ultY = listaDoble.ultimoNodoY()
                                window.addstr(ultY,ultX," ")
                                listaDoble.eliminarFinal()
                                imprimeAsteriscos(window,snake,listaDoble)  
                                ultX = listaDoble.ultimoNodoX()
                                ultY = listaDoble.ultimoNodoY()
                                window.addstr(ultY,ultX," ")
                                listaDoble.eliminarFinal()
                                valP-=1
                                print("izquierda: "+str(valP))
                                pts6=""
                                pts6 = "Score:"+str(valP)
                                window.addstr(0,4,"        ",curses.color_pair(6))
                                window.addstr(0,4,pts6,curses.color_pair(6))
                                pil. desapilar()
                                eliminarComida(comidaMala)
                                insertarComida(comidaMala)
                                mostrarComidaM(window,comidaMala)
                        else:
                                imprimeAsteriscos(window,snake,listaDoble)  
                                window.addstr(ultY,ultX," ")    
                                listaDoble.eliminarFinal()   
                                eliminarComida(comidaMala)
                                insertarComida(comidaMala)
                                mostrarComidaM(window,comidaMala)    
                    else:
                       
                        imprimeAsteriscos(window,snake,listaDoble)  
                        window.addstr(ultY,ultX," ")    
                        listaDoble.eliminarFinal()
                else:
                    #choca y pierde    
                    choque = choqueSnake(window,listaDoble,fila)
                    if(choque == True and listaDoble.tamanio>=4):
                        salida = 0
                        perder(window)
                        fila.encolar(Usr,valP)
                        #limpiarParaJuegoNuevo(listaDoble,listaComida,comidaMala,pil)
                    listaDoble.agregarPrincipio(posX,posY)
                    if(posX==posCX and posY==posCY):
                        imprimeAsteriscos(window,snake,listaDoble)  
                        window.addstr(ultY,ultX," ")
                        curses.beep( )
                        valP+=1
                        print("izquierda: "+str(valP))
                        pts7=""
                        pts7 = "Score:"+str(valP)
                        window.addstr(0,4,"        ",curses.color_pair(6))
                        window.addstr(0,4,pts7,curses.color_pair(6))
                        pil.apilar(posCX,posCY)
                        eliminarComida(listaComida)
                        insertarComida(listaComida)
                        mostrarComida(window,listaComida)
                    elif(posX==posMX and posY==posMY):
                        if(listaDoble.tamanio>3 and valP>0):
                                ultX = listaDoble.ultimoNodoX()
                                ultY = listaDoble.ultimoNodoY()
                                window.addstr(ultY,ultX," ")
                                listaDoble.eliminarFinal()
                                imprimeAsteriscos(window,snake,listaDoble)  
                                ultX = listaDoble.ultimoNodoX()
                                ultY = listaDoble.ultimoNodoY()
                                window.addstr(ultY,ultX," ")
                                listaDoble.eliminarFinal()
                                valP-=1
                                pts8=""
                                pts8 = "Score:"+str(valP)  
                                window.addstr(0,4,"         ",curses.color_pair(6))   
                                window.addstr(0,4,pts8,curses.color_pair(6))
                                pil. desapilar()
                                eliminarComida(comidaMala)
                                insertarComida(comidaMala)
                                mostrarComidaM(window,comidaMala)
                        else:
                                imprimeAsteriscos(window,snake,listaDoble)  
                                window.addstr(ultY,ultX," ")    
                                listaDoble.eliminarFinal()   
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
                   #choca y pierde
                   choque = choqueSnake(window,listaDoble,fila)
                   if(choque == True and listaDoble.tamanio>=4):
                        salida = 0
                        perder(window)
                        fila.encolar(Usr,valP)
                        #limpiarParaJuegoNuevo(listaDoble,listaComida,comidaMala,pil)
                   choqueSnake(window,listaDoble,fila)
                   listaDoble.agregarPrincipio(posX,posY)
                   if(posX==posCX and posY==posCY):
                        imprimeAsteriscos(window,snake,listaDoble)  
                        window.addstr(ultY,ultX," ")
                        curses.beep( )
                        valP+=1
                        print("arriba: "+str(valP))
                        pts9=""
                        pts9 = "Score:"+str(valP)
                        
                        window.addstr(0,4,"        ",curses.color_pair(6))
                        window.addstr(0,4,pts9,curses.color_pair(6))
                        pil.apilar(posCX,posCY)
                        eliminarComida(listaComida)
                        insertarComida(listaComida)
                        mostrarComida(window,listaComida)
                   elif(posX==posMX and posY==posMY):
                        if(listaDoble.tamanio>3 and valP>0):
                                ultX = listaDoble.ultimoNodoX()
                                ultY = listaDoble.ultimoNodoY()
                                window.addstr(ultY,ultX," ")
                                listaDoble.eliminarFinal()
                                imprimeAsteriscos(window,snake,listaDoble)  
                                ultX = listaDoble.ultimoNodoX()
                                ultY = listaDoble.ultimoNodoY()
                                window.addstr(ultY,ultX," ")
                                listaDoble.eliminarFinal()
                                valP-=1
                                print("arriba: "+str(valP))
                                pts10 = ""
                                pts10 = "Score:"+str(valP) 
                                
                                window.addstr(0,4,"         ",curses.color_pair(6))            
                                window.addstr(0,4,pts10,curses.color_pair(6))
                                pil. desapilar()
                                eliminarComida(comidaMala)
                                insertarComida(comidaMala)
                                mostrarComidaM(window,comidaMala)
                        else:
                                imprimeAsteriscos(window,snake,listaDoble)  
                                window.addstr(ultY,ultX," ")    
                                listaDoble.eliminarFinal()   
                                eliminarComida(comidaMala)
                                insertarComida(comidaMala)
                                mostrarComidaM(window,comidaMala)    
                   else:
                        imprimeAsteriscos(window,snake,listaDoble)  
                        window.addstr(ultY,ultX," ")    
                        listaDoble.eliminarFinal()
                else:
                   #choca y pierde     
                   choque = choqueSnake(window,listaDoble,fila)
                   if(choque == True and listaDoble.tamanio>=4):
                        salida = 0
                        perder(window)
                        fila.encolar(Usr,valP)
                        #limpiarParaJuegoNuevo(listaDoble,listaComida,comidaMala,pil)
                   listaDoble.agregarPrincipio(posX,posY)
                   if(posX==posCX and posY==posCY):
                        imprimeAsteriscos(window,snake,listaDoble)  
                        window.addstr(ultY,ultX," ")
                        curses.beep( )
                        valP+=1
                        print("arriba: "+str(valP))
                        pts11=""
                        pts11 = "Score:"+str(valP)
                        
                        window.addstr(0,4,"        ",curses.color_pair(6))
                        window.addstr(0,4,pts11,curses.color_pair(6))
                        pil.apilar(posCX,posCY)
                        eliminarComida(listaComida)
                        insertarComida(listaComida)
                        mostrarComida(window,listaComida)
                   elif(posX==posMX and posY==posMY):
                        if(listaDoble.tamanio>3 and valP>0):
                                ultX = listaDoble.ultimoNodoX()
                                ultY = listaDoble.ultimoNodoY()
                                window.addstr(ultY,ultX," ")
                                listaDoble.eliminarFinal()
                                imprimeAsteriscos(window,snake,listaDoble)  
                                ultX = listaDoble.ultimoNodoX()
                                ultY = listaDoble.ultimoNodoY()
                                window.addstr(ultY,ultX," ")
                                listaDoble.eliminarFinal()
                                valP-=1
                                print("arriba: "+str(valP))
                                pts12=""
                                pts12 = "Score:"+str(valP)
                                window.addstr(0,4,"        ",curses.color_pair(6))
                                window.addstr(0,4,pts12,curses.color_pair(6))
                                pil. desapilar()
                                eliminarComida(comidaMala)
                                insertarComida(comidaMala)
                                mostrarComidaM(window,comidaMala)
                        else:
                                imprimeAsteriscos(window,snake,listaDoble)  
                                window.addstr(ultY,ultX," ")    
                                listaDoble.eliminarFinal()   
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
                   #choca y pierde
                   choque = choqueSnake(window,listaDoble,fila)
                   if(choque == True and listaDoble.tamanio>=4):
                        salida = 0
                        perder(window)
                        fila.encolar(Usr,valP)
                        #limpiarParaJuegoNuevo(listaDoble,listaComida,comidaMala,pil)
                   listaDoble.agregarPrincipio(posX,posY)
                   if(posX==posCX and posY==posCY):
                        imprimeAsteriscos(window,snake,listaDoble)  
                        window.addstr(ultY,ultX," ")
                        curses.beep( )
                        valP+=1
                        print("abajo: "+str(valP))
                        pts13=""
                        pts13 = "Score:"+str(valP)
                        
                        window.addstr(0,4,"         ",curses.color_pair(6))
                        window.addstr(0,4,pts13,curses.color_pair(6))
                        pil.apilar(posCX,posCY)
                        eliminarComida(listaComida)
                        insertarComida(listaComida)
                        mostrarComida(window,listaComida)
                   elif(posX==posMX and posY==posMY):
                        if(listaDoble.tamanio>3 and valP>0):
                                ultX = listaDoble.ultimoNodoX()
                                ultY = listaDoble.ultimoNodoY()
                                window.addstr(ultY,ultX," ")
                                listaDoble.eliminarFinal()
                                imprimeAsteriscos(window,snake,listaDoble)  
                                ultX = listaDoble.ultimoNodoX()
                                ultY = listaDoble.ultimoNodoY()
                                window.addstr(ultY,ultX," ")
                                listaDoble.eliminarFinal()
                                valP-=1
                                print("abajo: "+str(valP))
                                pts14=""
                                pts14 = "Score:"+str(valP)
                                
                                window.addstr(0,4,"         ",curses.color_pair(6))
                                window.addstr(0,4,pts14,curses.color_pair(6))
                                pil. desapilar()
                                eliminarComida(comidaMala)
                                insertarComida(comidaMala)
                                mostrarComidaM(window,comidaMala)
                        else:
                                imprimeAsteriscos(window,snake,listaDoble)  
                                window.addstr(ultY,ultX," ")    
                                listaDoble.eliminarFinal()   
                                eliminarComida(comidaMala)
                                insertarComida(comidaMala)
                                mostrarComidaM(window,comidaMala)
                   else:
                        imprimeAsteriscos(window,snake,listaDoble)  
                        window.addstr(ultY,ultX," ")    
                        listaDoble.eliminarFinal()    
                else:
                   #choca y pierde     
                   choque = choqueSnake(window,listaDoble,fila)
                   if(choque == True and listaDoble.tamanio>=4):
                        salida = 0
                        perder(window)
                        fila.encolar(Usr,valP)
                        #limpiarParaJuegoNuevo(listaDoble,listaComida,comidaMala,pil)
                   listaDoble.agregarPrincipio(posX,posY)
                   if(posX==posCX and posY==posCY):
                        imprimeAsteriscos(window,snake,listaDoble)  
                        window.addstr(ultY,ultX," ")
                        curses.beep( )
                        valP+=1
                        print("abajo: "+str(valP))
                        pts15=""
                        pts15 = "Score:"+str(valP)
                        
                        window.addstr(0,4,"        ",curses.color_pair(6))
                        window.addstr(0,4,pts15,curses.color_pair(6))
                        pil.apilar(posCX,posCY)
                        eliminarComida(listaComida)
                        insertarComida(listaComida)
                        mostrarComida(window,listaComida)
                   elif(posX==posMX and posY==posMY):
                        if(listaDoble.tamanio>3 and valP>0):
                                ultX = listaDoble.ultimoNodoX()
                                ultY = listaDoble.ultimoNodoY()
                                window.addstr(ultY,ultX," ")
                                listaDoble.eliminarFinal()
                                imprimeAsteriscos(window,snake,listaDoble)  
                                ultX = listaDoble.ultimoNodoX()
                                ultY = listaDoble.ultimoNodoY()
                                window.addstr(ultY,ultX," ")
                                listaDoble.eliminarFinal()
                                valP-=1
                                print("abajo: "+str(valP))
                                pts16=""
                                pts16 = "Score:"+str(valP)
                                window.addstr(0,4,"         ",curses.color_pair(6))
                                window.addstr(0,4,pts16,curses.color_pair(6))
                                pil. desapilar()
                                eliminarComida(comidaMala)
                                insertarComida(comidaMala)
                                mostrarComidaM(window,comidaMala)
                        else:
                                imprimeAsteriscos(window,snake,listaDoble)  
                                window.addstr(ultY,ultX," ")    
                                listaDoble.eliminarFinal()   
                                eliminarComida(comidaMala)
                                insertarComida(comidaMala)
                                mostrarComidaM(window,comidaMala)

                   else:
                        imprimeAsteriscos(window,snake,listaDoble)  
                        window.addstr(ultY,ultX," ")    
                        listaDoble.eliminarFinal()             
        elif(salida==112 or salida == 80):
            salida = 0     
            juegoN.estado = False
            print("pause")
    return valP              
                        

def titulo(window,texto,usr,punteo):
    window.clear()
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK) 
    pintarVentana(window)
    centro = round((60-len(texto))/2)
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

def evaluarNivel(punteo):
        if(punteo <= 5):
                return 200
        elif(punteo<=10):
                return 100       
        else:
                return 75 

def choqueSnake(window,listaDoble = object,fila = object):
        choque = False
        if(listaDoble.estaVacia()):
                return
        else:    
                aux = listaDoble.cabezaListaD.siguiente
                while(aux!=None):
                        cabezitaX = listaDoble.cabezaListaD.posX
                        cabezitaY = listaDoble.cabezaListaD.posY
                        if(cabezitaX == aux.posX and cabezitaY == aux.posY):
                                choque = True
                                return choque
                        aux = aux.siguiente    

def perder(window):
        texto = "G A M E  O V E R"
        window.clear()
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK) 
        window.attron(curses.color_pair(3))
        window.border(0)
        window.attroff(curses.color_pair(3))
        window.refresh() 
        centro = round((60-len(texto))/2)
        window.addstr(0,centro,texto,curses.color_pair(3))

def limpiarParaJuegoNuevo(listaD = object,comida = object,comidaMala = object,pil = object):
            if(listaD.estaVacia() is not True):
                listaD.cabezaListaD.siguiente = None
                listaD.cabezaListaD = None
            if(comida.estaVacia() is not True):
                comida.cabezaListaD.siguiente = None
                comida.cabezaListaD = None
            if(comidaMala.estaVacia() is not True):
                comidaMala.cabezaListaD.siguiente = None
                comidaMala.cabezaListaD = None
            if(pil.estaVacia() is not True):
                pil.head.siguiente = None
                pil.head = None           