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
        global g
        total_nodos = total_nodos + 1
        self.id = (total_nodos) 
        self.estado = ""
        self.valor = ""
        self.profundidad = 0
        self.heuristica = ""
        self.accion = ""
        self.nodo_grafo = nodo
        self.costo = 0
        self.coste = 0

        if(padre != ""):
            self.padre = padre
            self.profundidad = self.padre.profundidad + 1
            self.coste = g.get_arista(nodo.id, padre.nodo_arbol.id).length
            self.costo = self.padre.costo + self.coste
           
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

    def __init__(self, lista_objetivos, current_nodo): #la lista de objetivos, el estado anterior, el nodo
        self.lista_objetivos = lista_objetivos
        self.current_nodo = current_nodo  # current_nodo y nodo_objetivo son el id del nodo
        self.cadena = "(" + self.current_nodo.nodo_grafo.id + ",("+ str(self.lista_objetivos) + "))"
        self.cadena=self.cadena.replace(" ","")
        self.id = hashlib.md5(self.cadena.encode("utf-8")).hexdigest() #Montamos cadena encriptada en md5, que será el id del estado

    def toString(self):
        return self.cadena
        
def sucesor(nodo):
    global g
    global lista_objetivos
    nodos = []
    e = estado(lista_objetivos, nodo)
    if len(e.lista_objetivos) == 0: #Si no quedan nodos objetivos, se hace return
        return
    print(e.toString())
    adyacentes= SortedList()
    adyacentes = g.adyacencia.get(str(nodo.nodo_grafo.id)) #Recogemos los nodos adyacentes del nodo actual
    for adyacente in adyacentes: # Por cada nodo adyacente
        n = g.lista_nodos.get(adyacente)
        n_arbol = nodo_arbol(n, nodo)
        e2 = estado(e.lista_objetivos, n_arbol) # Creamos el siguiente estado, siendo el siguiente nodo, el nodo adyacente
        if adyacente in lista_objetivos: # Si el adyacente esta en la lista de objetivos, le eliminamos de dicha lista
            e2.lista_objetivos.remove(adyacente)   
        cadena = "(" + str(e.current_nodo) + "->" + str(adyacente) + ",(" + str(adyacente) + "," + str(e2.lista_objetivos) + "," + str(n_arbol.coste) + ")"
        cadena=cadena.replace(" ","")
        print(cadena)
        n_arbol.estado = e2
        nodos.append(n_arbol)
        #Siguiente adyacente
    return nodos

def algoritmoBusqueda():
    global solucion
    global frontera
    global estados_visitados
    global maxdepth
    global estrategia
    nodo = ""

    if (len(frontera) == 0) or solucion:
        nodo.estado.construir_camino()
        return

    if estrategia == "p":
        nodo = frontera.pop()
    if estrategia == "a":
        nodo = frontera[0]
        frontera.remove(0)
    if estrategia == "c":
        nodo = menor_coste()
        
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

def menor_coste():
    global frontera
    coste = 0
    for i in range(len(frontera)):
        n_coste = frontera[0].costo
        if n_coste < coste[0]:
            coste = (n_coste, i)
    
    n = frontera[coste[1]]
    frontera.remove(coste[1])
    return n

lista = ['1']
n = "0"
nodo = g.lista_nodos.get(n)

nodo_arb = nodo_arbol(nodo, "")
e = estado (lista, nodo_arb)
nodo_arb.estado = e
frontera.append(nodo_arb)
maxdepth = 1000

algoritmoBusqueda()

