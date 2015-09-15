__author__ = 'Cristina Barreno'

import sys
from collections import OrderedDict
import hashlib
import time
import datetime
import random
import md5

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

    #Declaracion de Caches
    cprueba=OrderedDict()
    cprotegida=OrderedDict()


    hits=0
    misses=0
    cantidad=len(listamd)

    to = datetime.datetime.now()

    for elemento in listamd:


        if len(cprotegida)==cacheprotegida:
            cprueba.popitem(last=False)#Elimina el LRU si la cache protegida esta llena

         #Si la cache tiene elementos y no esta llena
        if hash(elemento) in cprueba:    # Busca de hay un hit en la cache de prueba
            cprueba.pop(hash(elemento))
            cprotegida[hash(elemento)]=0
            hits+=1
        elif hash(elemento) in cprotegida: # Busca si el elemento se encuentra en la cache protegida se produce un hit
            cprotegida[hash(cprotegida.pop(hash(elemento)))]=0
            hits+=1
        else:  # se produce un miss
            if len(cprueba)<cacheprueba:
                cprueba[hash(elemento)]=0
                misses+=1
            elif len(cprueba)==cacheprueba:
                cprueba.popitem(last=False)
                cprueba[hash(elemento)]=0
                misses+=1
            if cacheprotegida==len(cprotegida) and len(cprueba)==0:
                cprotegida.popitem(last=True)



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

    valor = float((float(misses)/float(cantidad))*100)
    valorHit = float(float(misses-(int(cachesize)))/float(cantidad)*100)
    porce=37

    print 'Resultados:'
    print 'Miss rate:\t%0.2f%c (%d misses out of %d references)' % (valor,porce,misses,cantidad)
    print 'Miss rate (warm cache):\t%0.2f%c (%d misses out of %d references)' % (valorHit,porce,misses-int(cachesize),cantidad)



    #print cprotegida[6]==listamd[10] Compara 2 cadenas
