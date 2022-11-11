import task1
import hashlib
from sortedcontainers import *

g = task1.graph()
g.iniciar_grafo()

class estado:

    def __init__(self, graf, current_nodo, lista_objetivos):
        graf = task1.graph()
        self.graf = graf
        self.adyacencia = graf.adyacencia
        self.nodos_no_visitados = graf.nodos
        self.nodos_visitado = []
        self.lista_objetivos = lista_objetivos
        self.current_nodo = current_nodo
        self.nuevo_estado = []

def sucesor(e):
    
    adyacentes = SortedList()
    adyacentes = e.adyacencia.get(e.current_nodo)

    for adyacente in adyacentes:
        if adyacente in e.nodos_visitado:
            next
        e.lista_objetivos.append(adyacente)
        if adyacente in e.lista_objetivos:
            e.lista_objetivos.remove(adyacente)
            
        print("(",e.current_nodo,"->", adyacente, ",(", adyacente, e.lista_objetivos, ")")
        e2 = estado(g, adyacente, e.lista_objetivos)
        e.nuevo_estado.append(e2)
        if len(e.lista_objetivos) != 0:
            sucesor(e2)
    



current_nodo='0'
lista_objetivos = ['5','27','881','1200']

e = estado(g, current_nodo, lista_objetivos)

sucesor(e)



        



