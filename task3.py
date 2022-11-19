import task1, task2
from sortedcontainers import *
import hashlib

g = task1.graph()
g.iniciar_grafo()
lista_nodos = g.lista_nodos
nodos_visitados = []
frontera = []
solucion = False
lista_objetivos = []
total_nodos = -1

class nodo:

    def __init__(self, padre):
        self.id += total_nodos + 1   
        self.estado = task2.estado()
        self.valor = ""
        self.profundidad = 0
        self.heuristica = ""
        self.accion = ""

        if(padre != ""):
            self.padre = padre
            self.profundidad = self.padre.profundidad + 1
            self.costo = self.padre.co
    
    def camino(self):
        pass

    def toString(self):
        return("[" + self.id) + "][" + self.costo + "," + self.estado.id + "," + self.padre.id + "," + self.accion + "," + self.profundidad + "," + self.heuristica + "," + self.valor + "]"


def algoritmoBusqueda(nodo):

    if len(frontera) != 0 & solucion:
        return
    
    e = task2.estado(g, lista_objetivos, nodo)

    if nodo.id in lista_objetivos:
        pass

n = nodo("")

lista = ['30', '60', '1300']
e = task2.estado(lista, )

frontera.append(nodo.id)

    