import sys

# Para obtener los parametros  enviados mediante consola
count=0
doc=''
tam=0
tipo=''
def RecorrerDoc(documento):
	print tam
	d=(linea for i,linea in enumerate(documento) if i<=tam)
	for l in d:
		print l
		continue
	return


def ObtenerParametros(sys):
	for x in sys:
		global count,doc,tam,tipo
		if count == 0:
			print x
			count=count+1
		else:
			if count == 1:
				doc=x
				print x
				count=count+1
			else:
				if count == 2:
					tipo=x
					print x
					count=count+1
				else:
					if count == 3:
						tam=int(x)
						print x
						count=count+1
	print "Evaluando una cache "+ tipo +" con "+ str(tam) +" entradas."
	print "Resultados:"
	return

ObtenerParametros(sys.argv)

archivo=open(doc, 'r')

print "funca"
RecorrerDoc(archivo)

archivo.close()

	