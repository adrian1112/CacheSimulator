from collections import deque
from random import choice
import time
 
class Memoria:
    def ejecuta(memoria, secuencia):
        fallos = 0
        for programa in secuencia:
            hay_fallo = memoria.add(programa)
            if hay_fallo:
                fallos += 1
        print('\nTasa de fallos = %s/%s\n\n' % (fallos, len(secuencia)))
 
secuencia = [2,2,3,1,1,3,4,5,1,1,2,3,4]
class MemoriaFIFO(Memoria):
    def __init__(self, i):
            self.cola = deque([])
            self.marcos = [False] * i
    def add(self, programa):
        fallo = 0
        # Fallo de pagina
        if not programa in self.marcos:
            fallo = 1
            if not False in self.marcos:
                # Borramos el primero de la cola
                indice = self.marcos.index(self.cola.popleft())
                self.marcos[indice] = False
 
            self.marcos[self.marcos.index(False)] = programa
 
        # Insertamos el programa en la cola
        if not programa in self.cola:
            self.cola.append(programa)
 
        return fallo
        
start_time = time.time()
contenido = []
sinRepetir = []
diccionario = {}
archivo = open("workload.txt","r")
for linea in archivo:
	linea = linea.rstrip('\n')
	contenido.append(linea)
sinRepetir = list(set(contenido))
numero = 1
for texto in sinRepetir:
	diccionario[texto] = numero 
	numero +=1
elapsed_time = time.time() - start_time
print("Elapsed time: %.10f seconds." % elapsed_time)
m3 = MemoriaFIFO(3)
ejecuta(m3,secuencia)