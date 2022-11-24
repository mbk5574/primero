import task1
import task2
from sortedcontainers import *
import hashlib

g = task1.graph()
g.iniciar_grafo()
lista_nodos = g.lista_nodos
estados_visitados = []
frontera = []
solucion = False
lista_objetivos = []
total_nodos = -1

class nodo_arbol:

    def __init__(self, nodo, padre):
        self.nodo = lista_nodos.get(nodo.id)
        self.id += (total_nodos + 1)
        total_nodos = total_nodos + 1   
        self.estado = task2.estado()
        self.valor = ""
        self.profundidad = 0
        self.heuristica = ""
        self.accion = ""
        nodo_grafo = lista_nodos.get(self.nodo.id)

        if(padre != ""):
            self.padre = padre
            self.profundidad = self.padre.profundidad + 1
            self.costo = self.padre.costo+self.costo
    
    def camino(self):
        pass

    def toString(self):
        return("[" + self.id) + "][" + self.costo + "," + self.estado.id + "," + self.padre.id + "," + self.accion + "," + self.profundidad + "," + self.heuristica + "," + self.valor + "]"


def algoritmoBusqueda(nodo, maxdepth):

    if (len(frontera) == 0) or solucion:
        nodo.estado.construir_camino()
        return
    
    nodo = frontera.pop

    if nodo.id in lista_objetivos:
        solucion = True
    elif (nodo.profundidad <= maxdepth) & (nodo.estado not in estados_visitados):
        estados_visitados.append(nodo.estado)
        estados = expandir(nodo.estado)
        for n in frontera:
            algoritmoBusqueda(nodo, maxdepth)
    else:
        algoritmoBusqueda(nodo, maxdepth)

def expandir(e):
    estados = task2.sucesor(e)
    return estados


lista = ['30']
n = "0"

nodo = nodo_arbol(n, "")
nodo.costo = 0
e = task2.estado(g, lista, "", nodo, "")
nodo.estado = e;
maxdepth = 3

frontera.append(n)

algoritmoBusqueda(nodo, maxdepth)

    