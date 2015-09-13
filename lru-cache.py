import time
import sys
import collections

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


def usage():
    print("usage: lru_cache_test.py lru_cache.py")

if __name__ == "__main__":
	
	mod = (sys.argv[1])
	entrada = (sys.argv[3])
	algoritmo = sys.argv[2]
	fallos = 0
	cantidad = 0
	contenido = list()
	archivo = open(mod,"r")
	if algoritmo == "LRU":
		print 'Evaluando una cache LRU con %d entradas.' % int(entrada) 
		lru = LRUCache(int(entrada),fallos)
		for linea in archivo:
			linea = linea.rstrip('\n')
			contenido.append(linea)
		with Tiempo() as t:
			for sentencia in contenido:
				cantidad +=1
				lru.establecer(sentencia,0)	
		print('lrucache took %.03f sec' % t.interval)
		print lru.fallos
		print cantidad
		base = lru.fallos
		valor = float((float(base)/float(cantidad))*100)
		valorHit = float(float(base-(int(entrada)))/float(cantidad)*100)
		porce = 37
		print 'Resultados:' 
		print 'Miss rate:\t%0.2f%c (%d misses out of %d references)' % (valor,porce,lru.fallos,cantidad)
		print 'Miss rate (warm cache):\t%0.2f%c (%d misses out of %d references)' % (valorHit,porce,lru.fallos-int(entrada),cantidad) 