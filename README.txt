Autores: Cristina Barreno, Adrian Aguilar, Marlon Loayza, Kevin Filella

Para ejecutarla en la consola de linux debera escribir lo siguiente:

			python Cache.py nombrearchivo politica cachesize extraparameter


- Politicas disponibles son las siguientes LRU, OPTIMO, CLOCK, SLRU
- El parametro extra solo es aplicable cuando la politica de reemplazo es la SLRU, para todas las demás solo serán necesario 3 parametros.
- El parametro extraparameter en la politica SLRU, corresponde al tamaño de la cache protegida, la cual el algoritmo exige que sea ingresado por parametro.

Ejemplo  para LRU:

			python Cache.py workload.txt LRU 600000

Ejemplo para SLRU:
			python Cache.py workload.txt LRU 600000 200000
			
Ejemplo para CLOCK:
			python Cache.py workload.txt Clock 600000
			
Ejemplo para Optimo:
			python Cache.py workload.txt Optimo 600000

El codigo estará disponible en el repositorio de github:

https://github.com/adrian1112/CacheSimulator
