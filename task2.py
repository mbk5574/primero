import task1, task3
import hashlib
from sortedcontainers import *

class estado:

    def __init__(self, graf, lista_objetivos, current_nodo = task3.nodo()):
        graf = task1.graph()
        self.graf = graf
        self.adyacencia = graf.adyacencia
        self.nodos_no_visitados = graf.nodos
        self.lista_objetivos = lista_objetivos
        self.current_nodo = current_nodo
        self.nuevo_estado = []
        self.next_nodo = ""
        self.id = str(current_nodo.id)
        self.id = hashlib.md5(self.id[(len(self.id) - 6): len(self.id)].encode("utf-8")).hexdigest()
    






        



