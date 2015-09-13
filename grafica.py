import matplotlib.pyplot as plt
import numpy as np
archivo = open("datos.txt","r")
plt.figure() 
ejex = list()
ejey = list()
for linea in archivo:
	linea = linea.rstrip("\n")
	split = linea.split(",")
	ejex.append(split[0])
	ejey.append(split[1])
indice = np.arange(len(ejey))   # Declara un array
plt.xticks(indice,ejex)
plt.plot(ejey, marker='o', linestyle='-', color='g', label = "LRU")
plt.title("Less Recent Used")
plt.xlabel("Cache Size")
plt.ylabel("Miss Rate")
plt.legend(loc="upper left")
plt.plot(ejey)
plt.show()