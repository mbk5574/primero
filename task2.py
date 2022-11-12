import task1
import hashlib
from sortedcontainers import *

class estado:

    def __init__(self, graf, current_nodo, lista_objetivos):
        graf = task1.graph()
        self.graf = graf
        self.adyacencia = graf.adyacencia
        self.nodos_no_visitados = graf.nodos
        self.lista_objetivos = lista_objetivos
        self.current_nodo = current_nodo
        self.nuevo_estado = []
        self.id = ""
    






        



