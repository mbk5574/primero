import task1
from sortedcontainers import *
import hashlib

g = task1.graph()
g.iniciar_grafo()
lista_nodos = g.lista_nodos
estados_visitados = []
frontera = []
solucion = False
lista_objetivos = []
total_nodos = 0
estrategia = "p" #p= profundidad, a = anchura, c = coste uniforme

class nodo_arbol:

    def __init__(self, nodo, padre):
        global total_nodos
        global estrategia
        total_nodos = total_nodos + 1
        self.id = (total_nodos) 
        self.estado = ""
        self.valor = ""
        self.profundidad = 0
        self.heuristica = ""
        self.accion = ""
        self.nodo_grafo = nodo
        self.costo = 0

        if(padre != ""):
            self.padre = padre
            self.profundidad = self.padre.profundidad + 1
            self.costo = self.padre.costo+self.costo

        if estrategia == "p":
            self.valor = 1/(self.profundidad + 1)
        elif estrategia == "a":
            self.valor = self.profundidad
        elif estrategia == "c":
            self.valor = self.costo
        else:
            print("Escribe bien la estrategia")
    
    def camino(self):
        pass

    def toString(self):
        return("[" + self.id) + "][" + self.costo + "," + self.estado.id + "," + self.padre.id + "," + self.accion + "," + self.profundidad + "," + self.heuristica + "," + self.valor + "]"


class estado:

    def __init__(self, g, lista_objetivos, estado_anterior, current_nodo, nodo_objetivo):
        self.g = g
        self.lista_objetivos = lista_objetivos
        self.nodo_objetivo= nodo_objetivo
        self.current_nodo = current_nodo
        self.cadena= ""
        if nodo_objetivo != "":
            arista = self.g.get_arista(self.current_nodo.nodo_grafo.id, self.nodo_objetivo.nodo_grafo.id)
            self.coste = arista.length
            cadena = "(" + str(self.current_nodo.id) + "->" +str(self.nodo_objetivo.nodo_grafo.id)+",("+ str(self.nodo_objetivo.nodo_grafo.id) + str(self.lista_objetivos) + "),"+str(self.nodo_objetivo.costo)+")"
            self.cadena=cadena.replace(" ","")
            self.id = hashlib.md5(cadena.encode("utf-8")).hexdigest()
            self.estado_anterior = estado_anterior
        else:
            self.coste = 0
           
    def construir_camino(self):
        cadena = ""
        e = self
        while(e.estado_anterior != ""):
            cadena = "->" + e.estado_anterior.current_nodo.id
            e = e.estado_anterior
        #cadena = cadena[2, len(cadena)]
        print(cadena)

def sucesor(nodo = nodo_arbol):
    if len(nodo.estado.lista_objetivos) == 0: #Si no quedan nodos objetivos, se hace return
        return

    e = nodo.estado
    nodos = []
    adyacentes= SortedList()
    adyacentes = e.g.adyacencia.get(str(nodo.nodo_grafo.id)) #Recogemos los nodos adyacentes del nodo actual
    for adyacente in adyacentes: # Por cada nodo adyacente
        a = nodo.estado.g.lista_nodos.get(adyacente)
        n = nodo_arbol(a, nodo)
        e2 = estado(e.g, e.lista_objetivos, e, nodo, n) # Creamos el siguiente estado, siendo el siguiente nodo, el nodo adyacente
        if adyacente in e2.lista_objetivos: # Si el adyacente esta en la lista de objetivos, le eliminamos de dicha lista
            e2.lista_objetivos.remove(adyacente)   
        
        cadena = "(" + str(e.current_nodo) + "->" + str(adyacente) + ",(" + str(adyacente) + "," + str(e2.lista_objetivos) + "," + str(e2.coste) + ")"
        cadena=cadena.replace(" ","")
        n.estado = e2
        nodos.append(n)
        #Siguiente adyacente
    return nodos


def algoritmoBusqueda():
    global solucion
    global frontera
    global estados_visitados
    global maxdepth
    global estrategia
    if (len(frontera) == 0) or solucion:
        nodo.estado.construir_camino()
        return
    if estrategia == "p":
        nodo = frontera.pop()
    if estrategia == "a":
        nodo = frontera.remove(0)
    if estrategia == "c":
        #nodo = frontera.elquemenorcostetenga
        pass
    print(nodo.estado.cadena)
    if nodo.nodo_grafo.id in nodo.estado.lista_objetivos:
        nodo.estado.lista_objetivos.remove(nodo.nodo_grafo.id)
        solucion = True
    elif (nodo.profundidad <= maxdepth) & (nodo.estado not in estados_visitados):
        estados_visitados.append(nodo.estado)
        expandir(nodo)
        algoritmoBusqueda()
    else:
        algoritmoBusqueda()

def expandir(nodo):
    nodos = sucesor(nodo)
    sorted(nodos, key= lambda x: x.valor)
    for i in range(len(nodos)):
        frontera.append[nodos[i]]

def ordenar(nodo):
    global frontera
    for i in range(len(frontera)):
        try:
            if (nodo.valor < frontera[i].valor) & (nodo.valor > frontera[i+1].valor):
                frontera.insert(i+1, nodo)
        except IndexError:
            frontera.append(nodo)

lista = ['1']
n = "0"
nodo = g.lista_nodos.get(n)
e = estado (g, lista, "", nodo, "")
e.coste = 0
nodo_arb = nodo_arbol(nodo, "")

adyacentes = g.adyacencia.get(str(n))
for ad in adyacentes:
    add = g.lista_nodos.get(ad)
    adyacente = nodo_arbol(add, nodo_arb)
    e1 = estado(g, lista, e, nodo_arb, adyacente)
    adyacente.estado = e
    frontera.add(adyacente)

maxdepth = 1000

algoritmoBusqueda()

