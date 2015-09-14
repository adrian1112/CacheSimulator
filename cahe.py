__author__ = 'Cristina Barreno'

import sys
import collections
import time
import datetime


if __name__ == "__main__":
#Guardar Parametro recibidos por consola
    if len(sys.argv) != 5:
        print "La cantidad de argumentos ingresada no es correcta"
    file = sys.argv[1]
    action = sys.argv[2]
    cachesize = sys.argv[3]
    cacheprotegida= int(sys.argv[4]) #Tamanio de la cache de prueba enviado por paramametro
    cacheprueba= int(cachesize)-cacheprotegida#Tamanio de la cache prueba

    print cacheprotegida
    print cacheprueba

    #Lectura de archivo y se guarda en una lista
    archi=open(file,'r')
    listamd=archi.readlines()
    archi.close()

    cprotegida = collections.deque(maxlen=cacheprotegida)
    cprueba = collections.deque(maxlen=cacheprueba)
    hits=0
    misses=0

    to = datetime.datetime.now()

    for elemento in listamd:
        if len(cprotegida)==cprotegida.maxlen:
            cprueba.popleft() #Elimina el LRU si la cache protegida esta llena

         #Si la cache tiene elementos y no esta llena
        if elemento in cprueba:    # Busca de hay un hit en la cache de prueba
            cprueba.remove(elemento)
            cprotegida.appendleft(elemento)
            hits+=1
        elif elemento in cprotegida: # Busca si el elemento se encuentra en la cache protegida se produce un hit
            cprotegida.appendleft(cprotegida.remove(elemento))
            hits+=1
        else:  # se produce un miss
            if len(cprueba)<cprueba.maxlen:
                cprueba.append(elemento)
                misses+=1
            elif len(cprueba)==cprueba.maxlen:
                cprueba.popleft()
                cprueba.append(elemento)
                misses+=1
            if cprotegida.maxlen>1 and cprueba.maxlen==0:
                cprotegida.pop()


    #print 'cacheProtegida'
    #for elemento in cprotegida:
    #    print elemento

    #print 'cachePrueba'
    #for elemento in cprueba:
    #    print elemento

    print 'Hits: ' + str(hits)
    print 'Miss: ' + str(misses)

    tf = datetime.datetime.now()
    t = tf - to

    print str(t)



    #print cprotegida[6]==listamd[10] Compara 2 cadenas
