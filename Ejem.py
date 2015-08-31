#!/usr/bin/python

class NoCache:
 def __init__(self):
  self.lista = range(1,900000)
 
 def getLista(self):
  return self.lista
  
 def setLista(self,value):
  lista.append(self.value)
 
 def getMedia(self):
  return reduce((lambda n,m:n+m),self.lista) / len(self.lista)
 

class Cache:
 def __init__(self):
  self.lista = range(1,900000)
  self.__actualizado = False
 
 def getLista(self):
  return self.lista
  
 def setLista(self,value):
  self.__actualizado = False
  lista.append(self.value)
 
 def getMedia(self):
  if self.__actualizado:
   return self.__sumaCache
  else:
   self.__sumaCache = reduce((lambda n,m:n+m),self.lista) / len(self.lista)
   self.__actualizado = True
   return self.__sumaCache
 

n = NoCache()
for i in range(5):
 print n.getMedia()
 
 
c = Cache()
for i in range(5):
 print c.getMedia()