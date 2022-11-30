import task1
from sortedcontainers import *
import hashlib
import sys

g = task1.graph()
g.iniciar_grafo()
lista_nodos = g.lista_nodos
estados_visitados = []
frontera = []
solucion = False
lista_objetivos = []
total_nodos = 0
estrategia = "" #p= profundidad, a = anchura, c = coste uniforme
maxdepth = -1

for i in range(len(sys.argv)):
    if sys.argv[i] == "-c":
        estrategia = "c"
    elif sys.argv[i] == "-p":
        estrategia = "p"
    elif sys.argv[i] == "-a":
        estrategia = "a"
    elif sys.argv[i] == "-m":
        try:
            maxdepth = int(sys.argv[i+1])
        except IndexError:
            raise IndexError("En la opcion maxdepth \"-m\" tienes que poner despues un numero entero")
        except TypeError:
            raise TypeError("El numero de maxdepth debe ser un entero mayor que 0")
        except ValueError:
            raise ValueError("El numero de maxdepth debe ser un entero mayor que 0")

class nodo_arbol:

    def __init__(self, nodo, padre):
        global total_nodos
        global estrategia
        global g
        total_nodos = total_nodos + 1
        self.id = (total_nodos) 
        self.estado = ""
        self.profundidad = 0
        self.heuristica = ""
        self.accion = ""
        self.nodo_grafo = nodo
        self.costo = 0
        self.coste = 0
        self.padre = padre

        if(self.padre != ""):
            
            self.profundidad = self.padre.profundidad + 1
            self.coste = g.get_arista(padre.nodo_grafo.id, nodo.id).length
            self.costo = float(self.padre.costo) + float(self.coste)
           
        if estrategia == "p":
            self.valor = 1/(self.profundidad + 1)
        elif estrategia == "a":
            self.valor = self.profundidad
        elif estrategia == "c":
            self.valor = self.costo
        else:
            print("Escribe bien la estrategia")
    
    def camino(self):
        cadena = ""
        e = self.estado
        p = self
        while p != "":
            cadena = cadena + "<-" + str(p.nodo_grafo.id)
            p = p.padre
        cadena = cadena.replace(" ", "")
        cadena = cadena[2: int(len(cadena))]
        cadena = "camino: " + cadena
        print(cadena)
    def toString(self):
        return("[" + self.id) + "][" + self.costo + "," + self.estado.id + "," + self.padre.id + "," + self.accion + "," + self.profundidad + "," + self.heuristica + "," + self.valor + "]"


class estado:

    def __init__(self, lista_objetivos, current_nodo, estado_anterior): #la lista de objetivos, el estado anterior, el nodo
        self.lista_objetivos = lista_objetivos
        self.current_nodo = current_nodo  # current_nodo y nodo_objetivo son el id del nodo
        self.cadena = "(" + self.current_nodo.nodo_grafo.id + ",("+ str(self.lista_objetivos) + "))"
        self.cadena=self.cadena.replace(" ","")
        self.id = hashlib.md5(self.cadena.encode("utf-8")).hexdigest() #Montamos cadena encriptada en md5, que será el id del estado
        self.estado_anterior = estado_anterior
    def toString(self):
        return self.cadena
        
def sucesor(nodo):
    global g
    global lista_objetivos
    nodos = []
    e = nodo.estado
    if len(e.lista_objetivos) == 0: #Si no quedan nodos objetivos, se hace return
        return
    adyacentes= SortedList()
    adyacentes = g.adyacencia.get(str(nodo.nodo_grafo.id)) #Recogemos los nodos adyacentes del nodo actual
    try:
        for adyacente in adyacentes: # Por cada nodo adyacente
        
            n = g.lista_nodos.get(adyacente)
            n_arbol = nodo_arbol(n, nodo)
            e2 = estado(e.lista_objetivos, n_arbol, e) # Creamos el siguiente estado, siendo el siguiente nodo, el nodo adyacente
            if adyacente in e2.lista_objetivos: # Si el adyacente esta en la lista de objetivos, le eliminamos de dicha lista
                e2.lista_objetivos.remove(adyacente)
                n_arbol.estado = e2
                n_arbol.camino()
                #nodo.estado.lista_objetivos.remove(adyacente)  
            cadena = "(" + str(e.current_nodo.nodo_grafo.id) + "->" + str(adyacente) + ",(" + str(adyacente) + "," + str(e2.lista_objetivos) + ")," + str(n_arbol.coste) + ")"
            cadena=cadena.replace(" ","")
            n_arbol.estado = e2
            nodos.append(n_arbol)
            #Siguiente adyacente
    except TypeError:
        pass
    
    return nodos

def algoritmoBusqueda():
    global solucion
    global frontera
    global estados_visitados
    global maxdepth
    global estrategia
    nodo = ""
    
    while True:
     
        if (len(frontera) == 0) or solucion:
            break

        if estrategia == "p":
            nodo = frontera.pop()
        elif estrategia == "a":
            nodo = frontera[0]
            frontera.remove(frontera[0])
        elif estrategia == "c":
            nodo = menor_coste()

        if len(nodo.estado.lista_objetivos) == 0:
            solucion = True
        
        if (((nodo.profundidad <= maxdepth) or (maxdepth == -1)) & (nodo.estado.id not in estados_visitados)):
            estados_visitados.append(nodo.estado.id)
            expandir(nodo)

        

def expandir(nodo):
    nodos = sucesor(nodo)
    try:
        sorted(nodos, key= lambda x: x.valor)
        for i in range(len(nodos)):
            frontera.append(nodos[i])
    except TypeError:
        pass

def menor_coste():
    global frontera
    coste = (0, 0)
    for i in range(len(frontera)):
        n_coste = frontera[0].costo
        if n_coste < coste[0]:
            coste = (n_coste, i)
    
    n = frontera[coste[1]]
    frontera.remove(frontera[coste[1]])
    return n

lista = ['1200']
n = "0"
nodo = g.lista_nodos.get(n)

nodo_arb = nodo_arbol(nodo, "")
e = estado (lista, nodo_arb, "")
nodo_arb.estado = e
frontera.append(nodo_arb)
if estrategia == "":
    raise Exception("Seleccione una estrategia")
algoritmoBusqueda()
