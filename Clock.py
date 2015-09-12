# --coding: utf-8 --
#!/usr/bin/env python

from sys import argv 

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
	cache = [] 		  
	p_f = 0     
	diccionario={}
	indice=0
	for i in range(len(pages)):
		page = pages[i]	
		if indice<tamCache:
			indice +=1
		else:
			indice =0

		if len(cache) < tamCache: 
			if (page in cache):
				diccionario[page]=1
			else:
				diccionario[page]=0
				cache.append(page)
				p_f += 1
		else:
			if (page in cache):
				if(diccionario.get(page)==0):
					diccionario[page]=1
			else:
				pag_elimi=cache[indice]
				if (diccionario.get(pag_elimi)==0):
					del diccionario[pag_elimi]
					cache.remove(pag_elimi)
					diccionario[page]=0
					cache.append(page)
				else:
					i=False
					while i==False:
						pag_elimi=cache[indice]
						if (diccionario.get(pag_elimi)==1):
							diccionario[pag_elimi]=0
							if indice <tamCache:
								indice += 1
							else:
								indice=0
						else:
							del diccionario[pag_elimi]
							diccionario[page]=0
							cache.remove(pag_elimi)
							cache.append(page)
							i=True
				p_f += 1 
	return p_f



sc_p_f = Clock(pages,600000)
print'Algortmo de reemplazo  Second Chance, Page Faults: ' + str(sc_p_f) 
