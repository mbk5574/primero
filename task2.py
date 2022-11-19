import task3
import hashlib
from sortedcontainers import *

class estado:

    def __init__(self, g, lista_objetivos, current_nodo = task3.nodo_arbol(),nodo_objetivo = task3.nodo_arbol()):
        self.g = g
        self.lista_objetivos = lista_objetivos
        self.nodo_objetivo= nodo_objetivo
        self.current_nodo = current_nodo

        self.coste = g.get_arista(current_nodo.nodo, nodo_objetivo.nodo).length
        cadena = "(" + self.current_nodo.id + "->" +self.nodo_objetivo.id+",("+ self.nodo_objetivo.id + self.lista_objetivos + "),"+self.nodo_objetivo.costo+")"
        cadena=cadena.replace(" ","")
        self.id = hashlib.md5(cadena.encode("utf-8")).hexdigest()
        