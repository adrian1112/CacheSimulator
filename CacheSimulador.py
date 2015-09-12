# --coding: utf-8 --
#!/usr/bin/env python

from sys import argv 

input_file = argv[1]
algoritmo= argv[2]
tam_cache=argv[3]
f = open(input_file)
pages = f.read()
f.close()


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
	cache = [] 		 
	p_f = 0 
	print("Evaluando una caché "+algoritmo+" con "+ tam_cache+" entradas. "+"\n")
	for i in range(len(pages)):
		page = pages[i]	
		if len(cache) < tamCache: 
			if not(page in cache):
				cache.append(page)
				p_f += 1 # Page Fault.
		else:
			if not(page in cache):
				indice = 0 
				for j in range(tamCache):
					mayor = Comparar(cache[j],pages[i:]) 
					if (mayor > indice):
						indice = mayor
					else:
						continue
					diccionario[indice] = cache[j] 
				paginaRemover = diccionario.get(indice) 
				try:
					cache[cache.index(paginaRemover)]=page
					p_f += 1 
				except:
					continue
	return p_f
			




p_fs = Optimal(pages,int(tam_cache))
print'Algortmo de reemplazo Optmo, Page Faults: ' + str(p_fs) 
