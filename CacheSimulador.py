# --coding: utf-8 --
#!/usr/bin/env python

import time
import sys
import hashlib
import md5
from collections import OrderedDict
import datetime

class LRUCache:
    def __init__(self, capacidad,fallos):
        self.cache = collections.OrderedDict()
        self.capacidad = capacidad
        self.fallos = fallos

    def obtener(self, clave):
        try:
            valor = self.cache.pop(clave)
            self.cache[clave] = valor
            return valor
        except KeyError:
            return -1

    def establecer(self, clave, valor):
		
        try:
            self.cache.pop(clave)            	
        except KeyError:
        		self.fallos +=1
        		if len(self.cache) >= self.capacidad:
        			self.cache.popitem(last=False)
        self.cache[clave] = valor
        
class Tiempo:
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start



def Comparar(pag_en_Cache,pages):
	try:
		index=pages.index(pag_en_Cache)
		return index
	except:
		return len(pages)

def Optimal(pages,N):
	tamCache = N   
	cache = OrderedDict() 
	p_f = 0 
	k=0
	print("Evaluando una caché "+algoritmo+" con "+ tam_cache+" entradas. "+"\n")
	for i in range(len(pages)):
		page = pages[i]	
		if len(cache) < tamCache: 
			if not (cache.has_key(page)):    
				cache[page]=k
				p_f += 1 
				k += 1
		else:
			if not (cache.has_key(page)): 
				indice = 0 
				ind=0
				pal=''
				
				for p, j  in cache.items():
					try:
						to=datetime.datetime.now()
						mayor = pages[i:].index(p) 
						tf = datetime.datetime.now()
						t = tf - to
						print t
					except:
						mayor = len(pages[i:])
						ind=j
						pal=p
						break
					if (mayor > indice ):
						indice = mayor
						ind=j
						pal=p
				try:	
					del cache[p]
					cache[page]=ind
					p_f += 1 
				except:
					pass
	return p_f


def Clock(pages,n):
	#pages = pages.split('\n')
	tamCache = n   
	cache = OrderedDict() 		  
	p_f = 0    
	hits = 0
	indice=0
	cantidad = len(pages)
	for i in range(cantidad):
		page = hash(pages[i])	
		# Al inicio, si cache no esta llena
		if len(cache) < tamCache: 	
			# Si pagina ya se encuentra en cache, se produce hit y bit=1 (second chance)
			if (page in cache):  	
				cache[page]=1
				hits += 1
			else:               	
			# Caso contrario, agrega la pagina con bit=0 y produce page fault
				cache[page]=0
				p_f += 1
		else:
			# Si cache ya esta llena y la pagina esta en cache
			if (page in cache):	
				# Cambia bit=0 a bit=1 y produce hit
				if(cache.get(page)==0): 
					cache[page]=1
					hits += 1
				# Si el bit ya estaba en 1, solo produce hit
				if(cache.get(page)==1): 
					hits += 1
			# Si pagina no esta en cache, analiza el bit de referencia
			else:
				# Si el bit es 1, le da segunda oportunidad y continua
				if(cache.get(page)==1):
					cache[page]=0
				# Si el bit es 0, remueve y agrega nueva pagina con bit=0
				else:
					cache.popitem(last=False) 
					cache[page]=0
					p_f += 1 
	return (p_f, hits, cantidad)

def SLRU(listamd,cacheprotegida):	
	
	#Declaracion de Caches
	cprueba=OrderedDict()
	cprotegida=OrderedDict()


	hits=0
	misses=0
	cantidad=len(listamd)

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
	return (hits,misses,cantidad)
			

if __name__ == "__main__":
	input_file = sys.argv[1]
	algoritmo= sys.argv[2]
	tam_cache=sys.argv[3]
	pages=[]
	f = open(input_file)
	for i in f:
		page=i.rstrip("\n")
		pages.append(hash(page))
	f.close()
	cantidad=len(pages)
	p_fs=0
	if algoritmo == "Optimo":
		with Tiempo() as t:
			p_fs = Optimal(pages,int(tam_cache))
		print('lrucache took %.03f sec' % t.interval)
		
		print p_fs
		print cantidad
		base = p_fs
		valor = float((float(base)/float(cantidad))*100)
		valorHit = float(float(base-(int(tam_cache)))/float(cantidad)*100)
		porce = 37
		print 'Resultados:' 
		print 'Miss rate:\t%0.2f%c (%d misses out of %d references)' % (valor,porce,p_fs,cantidad)
		#print 'Miss rate (warm cache):\t%0.2f%c (%d misses out of %d references)' % (valorHit,porce,p_fs-int(tam_cache),cantidad)
	
	if algoritmo == "LRU":
		entrada = tam_cache
		fallos = 0
		cantidad = 0
		contenido = list()
		archivo = open(input_file,"r")
		print 'Evaluando una cache LRU con %d entradas.' % int(entrada)		 
		lru = LRUCache(int(entrada),fallos)
		linea=archivo.readline()
		sentencia=linea.rstrip("\n")
		lru.establecer(sentencia,0)
		cantidad +=1
		to = datetime.datetime.now()
  		while linea != "":
  			linea=archivo.readline()
  			sentencia=linea.rstrip("\n")
			lru.establecer(sentencia,0)
			cantidad +=1	
		tf = datetime.datetime.now()
		t = tf-to
		print str(t)
		base = lru.fallos
		valor = float((float(base)/float(cantidad))*100)
		valorHit = float(float(base-(len(lru.cache)))/float(cantidad)*100)
		porce = 37
		print 'Resultados:' 
		print 'Miss rate:\t%0.2f%c (%d misses out of %d references)' % (valor,porce,lru.fallos,cantidad)
		#print 'Miss rate (warm cache):\t%0.2f%c (%d misses out of %d references)' % (valorHit,porce,cantidad-lru.fallos-len(lru.cache),cantidad) 
	if algoritmo == "Clock":
		to = datetime.datetime.now()
		sc_p_f, hits, cantidad = Clock(pages,int(tam_cache))
		tf = datetime.datetime.now()
		t = tf - to
		print'Algoritmo de reemplazo  Second Chance, Page Faults: ' + str(sc_p_f) + ' Hits: ' + str(cantidad-sc_p_f)
		print'Tiempo de ejecucion: '+str(t)
		missRate = float((float(sc_p_f)/float(cantidad)))*100
		print 'Hit rate: '+str(100-missRate)
		print 'Miss rate: '+str(missRate)
	if algoritmo =="SLRU":
		#Lectura de archivo y se guarda en una lista
		archi=open(input_file,'r')
		listamd=archi.readlines()
		archi.close()
		cacheprotegida= int(sys.argv[4]) #Tamanio de la cache de prueba enviado por paramametro
		cacheprueba= int(tam_cache)-cacheprotegida#Tamanio de la cache prueba
		to = datetime.datetime.now()
		hits,misses,cantidad=SLRU(listamd, cacheprotegida)
		print 'Hits: ' + str(hits)
		print 'Miss: ' + str(misses)
		tf = datetime.datetime.now()
		t = tf - to
		print str(t)
		valor = float((float(misses)/float(cantidad))*100)
		valorHit = float(float(misses-(int(tam_cache)))/float(cantidad)*100)
		porce=37
		print 'Resultados:'
		print 'Miss rate:\t%0.2f%c (%d misses out of %d references)' % (valor,porce,misses,cantidad)
		#print 'Miss rate (warm cache):\t%0.2f%c (%d misses out of %d references)' % (valorHit,porce,misses-int(tam_cache),cantidad)



		
