# --coding: utf-8 --
#!/usr/bin/env python

from sys import argv 
import hashlib
import md5
from collections import OrderedDict
import time
import datetime

input_file = argv[1]
algoritmo= argv[2]
tam_cache=argv[3]
f = open(input_file)
pages = f.read()
f.close()

# Second Chance 
def Clock(pages,n):
	pages = pages.split('\n')
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

to = datetime.datetime.now()
sc_p_f, hits, cantidad = Clock(pages,int(tam_cache))
tf = datetime.datetime.now()
t = tf - to
print'Algoritmo de reemplazo  Second Chance, Page Faults: ' + str(sc_p_f) + ' Hits: ' + str(cantidad-sc_p_f)
print'Tiempo de ejecucion: '+str(t)
missRate = float((float(sc_p_f)/float(cantidad)))*100
print 'Hit rate: '+str(100-missRate)
print 'Miss rate: '+str(missRate)
