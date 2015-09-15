# --coding: utf-8 --
#!/usr/bin/env python

import time
import sys




def Comparar(pag_en_Cache,pages):
	try:
		index=pages.index(pag_en_Cache)
		return index
	except:
		return len(pages)

def Optimal(pages,N):
	diccionario = {} 
	pages = pages.split("\n") 
	#pages = pages.split() 
	tamCache = N   
	cache = {}
	p_f = 0 
	k=0
	print("Evaluando una caché "+algoritmo+" con "+ tam_cache+" entradas. "+"\n")
	for i in range(len(pages)):
		page = pages[i]	
		#print cache.get(page)
		#print page
		#print len(cache)
		#print cache
		if len(cache) < tamCache: 
			if not (cache.has_key(page)):    #page in cache
				cache[page]=k
				p_f += 1 # Page Fault.
				k += 1
			
		else:
			if not (cache.has_key(page)): 
				indice = 0 
				ind=0
				for p, j  in cache.items():
					mayor = Comparar(p,pages[i:]) 
					if (mayor > indice):
						indice = mayor
						ind=j
					else:
						continue
					diccionario[indice] = p 
				paginaRemover = diccionario.get(indice) 
				try:
					cache[ind]=page             #cache.index(paginaRemover)
					p_f += 1 
				except:
					continue
	return p_f

class Tiempo:
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start
			

if __name__ == "__main__":
	input_file = sys.argv[1]
	algoritmo= sys.argv[2]
	tam_cache=sys.argv[3]
	f = open(input_file)
	pages = f.read()
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
		print 'Miss rate (warm cache):\t%0.2f%c (%d misses out of %d references)' % (valorHit,porce,p_fs-int(tam_cache),cantidad)  
