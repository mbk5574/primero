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
        self.lista_objetivos = lista_objetivos
        self.current_nodo = current_nodo
        self.nuevo_estado = []
        self.id = ""
        
def sucesor(e):
    if len(e.lista_objetivos) == 0:
        return
    if e.current_nodo in e.graf.nodos_visitado:
        return

    cadena = "(" + str(e.current_nodo) + "->" + "str(adyacente)" + ",(" + "str(adyacente)" + str(e.lista_objetivos) + ")"
    print(cadena)
       
    e.id = hashlib.md5(cadena.encode('utf-8')).hexdigest()
    print(e.id)

current_nodo='0'

lista_objetivos = SortedList(['33', '1200'])

e = estado(g, current_nodo, lista_objetivos)

sucesor(e)



        



