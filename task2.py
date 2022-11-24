import task3
import task1
import hashlib
from sortedcontainers import *

class estado:

    def __init__(self, g, lista_objetivos, estado_anterior, current_nodo = task3.nodo_arbol(),nodo_objetivo = task3.nodo_arbol()):
        self.g = g
        self.lista_objetivos = lista_objetivos
        self.nodo_objetivo= nodo_objetivo
        self.current_nodo = current_nodo
        self.coste = g.get_arista(current_nodo.nodo.id, nodo_objetivo.nodo.id).length
        self.estado_anterior = estado_anterior

        cadena = "(" + self.current_nodo.id + "->" +self.nodo_objetivo.id+",("+ self.nodo_objetivo.id + self.lista_objetivos + "),"+self.nodo_objetivo.costo+")"
        cadena=cadena.replace(" ","")
        self.id = hashlib.md5(cadena.encode("utf-8")).hexdigest()
        
    def construir_camino(self):
        cadena = ""
        e = self
        while(e.estado_anterior != ""):
            cadena = "->" + e.estado_anterior.current_nodo.id
            e = e.estado_anterior
        cadena = cadena[2, len(cadena)]
        print(cadena)

def sucesor(e):
    if len(e.lista_objetivos) == 0: #Si no quedan nodos objetivos, se hace return
        return

    estados = []
    adyacentes= SortedList()
    adyacentes = e.graf.adyacencia.get(str(e.current_nodo.nodo_grafo.id)) #Recogemos los nodos adyacentes del nodo actual
    for adyacente in adyacentes: # Por cada nodo adyacente
        e2 = estado(e.graf, e.lista_objetivos, e, e.current_nodo, adyacente) # Creamos el siguiente estado, siendo el siguiente nodo, el nodo adyacente
        if adyacente in e2.lista_objetivos: # Si el adyacente esta en la lista de objetivos, le eliminamos de dicha lista
            e2.lista_objetivos.remove(adyacente)   
        
        cadena = "(" + str(e.current_nodo) + "->" + str(adyacente) + ",(" + str(adyacente) + "," + str(e2.lista_objetivos) + "," + str(e2.coste) + ")"
        cadena=cadena.replace(" ","")
        print(cadena)
        estados.append(e2)
        #Siguiente adyacente
    return estados