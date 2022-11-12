import task1, task2
from sortedcontainers import *
import hashlib

g = task1.graph()
g.iniciar_grafo()

def sucesor(e):
    if len(e.lista_objetivos) == 0:
        return
    if e.current_nodo in e.graf.nodos_visitado:
        return

    adyacentes= SortedList()
    adyacentes = e.adyacencia.get(str(e.current_nodo))
    
    e.graf.nodos_visitado.append(e.current_nodo)

    for adyacente in adyacentes:
            
        
        if adyacente in e.lista_objetivos:
            e.lista_objetivos.remove(adyacente)

        cadena = "(" + str(e.current_nodo) + "->" + str(adyacente) + ",(" + str(adyacente) + "," + str(e.lista_objetivos) + ")"
        
        if len(e.lista_objetivos) != 0:
            print(cadena)
        
        e.id = hashlib.md5(cadena.encode('utf-8')).hexdigest()
   
        e2 = task2.estado(e.graf, adyacente, e.lista_objetivos)
        e2.graf.nodos_visitado = e.graf.nodos_visitado
        e.nuevo_estado.append(e2)
        sucesor(e2)

current_nodo='0'

lista_objetivos = SortedList(['33', '1200'])
print("(" + current_nodo + "," + str(lista_objetivos) + ")")
e = task2.estado(g, current_nodo, lista_objetivos)

sucesor(e)