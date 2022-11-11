import task1
import hashlib
from sortedcontainers import *

class estado:
    graf = ""
    nodos = ""
    nodos_por_visitar = ""
    current_nodo = ""

    def __init__(self, graf, current_nodo):
        self.graf = task1.grafo()
        self.graf = graf
        self.nodos = graf.adyacencia
        self.nodos_por_visitar = graf.nodos
        self.current_nodo = current_nodo
    
    def estado(self):
        print(self.current_nodo, "\n")
        int = self.nodos.find(self.current_nodo)
        self.nodos.
        a = SortedList()
        a = self.adyacencia.get(self.current_nodo)
        
        cadena = (self.current_nodo, a)


g = task1.grafo()
#print(g.adyacencia)
est = estado(g, 0)

est.estado()



