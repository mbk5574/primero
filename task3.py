import task1, task2
from sortedcontainers import *
import hashlib

g = task1.graph()
g.iniciar_grafo()
lista_nodos = g.lista_nodos


class frontera:

    def __init__(self):
        self.nodos = []

class nodo:

    def __init__(self):
        self.id += 1
        self.padre = nodo()
        self.estado = task2.estado()
        self.valor = ""
        self.profundidad = ""
        self.costo = ""
        self.heuristica = ""
        self.accion = ""
    
    def camino(self):
        pass

    def toString(self):
        return("[" + self.id) + "][" + self.costo + "," + self.estado.id + "," + self.padre.id + "," + self.accion + "," + self.profundidad + "," + self.heuristica + "," + self.valor + "]"


