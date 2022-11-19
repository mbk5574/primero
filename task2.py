import task3
import hashlib
from sortedcontainers import *

class estado:

    def __init__(self, lista_objetivos, current_nodo = task3.nodo()):

        self.lista_objetivos = lista_objetivos
        self.current_nodo = current_nodo
        cadena = "(" + self.current_nodo + "," + self.lista_objetivos + ")".replace(" ", "")
        self.id = hashlib.md5(cadena.encode("utf-8")).hexdigest()
        