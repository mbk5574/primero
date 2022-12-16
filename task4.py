import task1
from sortedcontainers import sortedlist
import hashlib
import sys

g = task1.graph()
g.iniciar_grafo()
lista_nodos = g.lista_nodos
estados_visitados = []
frontera = []
solucion = False
lista_objetivos = []
total_nodos = -1
ultimo = False
primero = True
estrategia = "A" #p= profundidad, a = anchura, c = coste uniforme

maxdepth = -1

for i in range(len(sys.argv)):
    if sys.argv[i] == "-c":
        estrategia = "c"
    elif sys.argv[i] == "-p":
        estrategia = "p"
    elif sys.argv[i] == "-a":
        estrategia = "a"
    elif sys.argv[i] == "-A":
        estrategia = "A"
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
        self.estado = None
        self.profundidad = 0
        self.heuristica = 0
        self.accion = None
        self.nodo_grafo = nodo
        self.costo = 0
        self.coste = 0
        self.padre = padre

        if(self.padre != None):
            
            self.profundidad = self.padre.profundidad + 1
            self.coste = g.get_arista(padre.nodo_grafo.id, nodo.id).length
            self.costo = round((float(self.padre.costo) + float(self.coste)), 2)
           
        if estrategia == "p":
            self.valor = 1/(self.profundidad + 1)
        elif estrategia == "a":
            self.valor = self.profundidad
        elif estrategia == "c":
            self.valor = self.costo
        elif estrategia == "A":
            self.valor = self.heuristica + self.costo
        else:
            print("Escribe bien la estrategia")
    
    def heuri(self, heur):
        self.heuristica = round(heur, 2)
        self.valor = round((self.costo + heur), 2)

    def camino(self):   
        global ultimo 
        global primero
        cadena = ""
        camino = []
        p = self
        h = None

        try:

            if ultimo:
                accion = "(" + str(self.padre.nodo_grafo.id) + "->" + str(self.nodo_grafo.id) + ")"
                estado = self.estado.id[(len(self.estado.id) -6): len(self.estado.id)]
                cadena = "[" + str(self.id) + "][" + str(p.costo) + "," + "[" + p.estado.toString() + "|" + str(estado) + "]" + "," + str(self.padre.id) + "," + accion + "," + str(self.profundidad) + "," + str(self.heuristica) + "," + str(self.valor) + "]"
            
                camino.append(cadena)

            while p is not None:
                try:
                    estado = p.estado.id[(len(p.estado.id) -6): len(p.estado.id)]
                    accion = "(" + str(p.padre.nodo_grafo.id) + "->" + str(p.nodo_grafo.id) + ")"
                    cadena = "[" + str(p.id) + "][" + str(p.costo) + "," + "[" + p.estado.toString() + "|" + str(estado) + "]" + "," + str(p.padre.id) + "," + accion + "," + str(p.profundidad) + "," + str(p.heuristica) + "," + str(p.valor) + "]"
                    cadena = cadena.replace(" ", "")
                    camino.append(cadena)
                except Exception:
                    cadena = ""
                h = p
                p = p.padre

            estado = h.estado.id[(len(h.estado.id) -6): len(h.estado.id)]
            if primero:
                
                primero = False
                
            cadena = "[" + str(h.id) + "][" + str(h.costo) + "," + "[" + h.estado.toString() + "|" + str(estado) + "]" + "," + str(h.profundidad) + "," + str(h.heuristica) + "," + str(h.valor) + "]"
            camino.append(cadena)   
         
            camino.reverse()
            for cad in camino:
                print(cad)
        except TypeError:
            pass 
             
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

    def heuristica(self):
        if self.estado_anterior == "":
            pass

def min_euclideo(nodo, lista_objetivos):
    global g
    dist_min = 0
    d = 0
    for i in range(len(lista_objetivos)):
        d = nodo.nodo_grafo.euclidea(g.lista_nodos.get(lista_objetivos[i]))
        if (d < dist_min) or (dist_min == 0):
            dist_min = d
    return dist_min

def objetivo(nodo):
    global ultimo
    if len(nodo.estado.lista_objetivos) != 0:
        nodo.padre = None
        ultimo = True
    if(estrategia == "A"):
        lista_n = []
        for node in nodo.estado.lista_objetivos:
            nodo_grafo = g.lista_nodos.get(node)   
            lista_n.append(nodo_grafo)
        d = min_euclidea_objetivos(lista_n)
        nodo.heuri(d)

    frontera.clear()
    frontera.append(nodo)
    estados_visitados.clear()
    algoritmoBusqueda()

def sucesor(nodo):
    global g
    global lista_objetivos
    global d1
    nodos = []
    e = nodo.estado
    if len(e.lista_objetivos) == 0: #Si no quedan nodos objetivos, se hace return
        return

    adyacentes= sortedlist.SortedList()
    adyacentes = g.adyacencia.get(str(nodo.nodo_grafo.id)) #Recogemos los nodos adyacentes del nodo actual
    try:
        for adyacente in adyacentes: # Por cada nodo adyacente
        
            n = g.lista_nodos.get(adyacente)
            n_arbol = nodo_arbol(n, nodo)
            
            e2 = estado(e.lista_objetivos, n_arbol, e) # Creamos el siguiente estado, siendo el siguiente nodo, el nodo adyacente
            n_arbol.estado = e2

            if estrategia == "A":
                d2 = min_euclideo(nodo, e2.lista_objetivos)
                if d1 <= d2:
                    n_arbol.heuri((d1*len(e2.lista_objetivos))) 
                else:
                    n_arbol.heuri((d2*len(e2.lista_objetivos))) 

            if adyacente in e.lista_objetivos: # Si el adyacente esta en la lista de objetivos, le eliminamos de dicha lista
                e.lista_objetivos.remove(adyacente)
                e2 = estado(e.lista_objetivos, n_arbol, e) # Creamos el siguiente estado, siendo el siguiente nodo, el nodo adyacente
                n_arbol.estado = e2
                n_arbol.camino()
                objetivo(n_arbol)
                
            cadena = "(" + str(e.current_nodo.nodo_grafo.id) + "->" + str(adyacente) + ",(" + str(adyacente) + "," + str(e2.lista_objetivos) + ")," + str(n_arbol.coste) + ")"
            cadena=cadena.replace(" ","")
            n_arbol.estado = e2

            nodos.append(n_arbol)
            #Siguiente adyacente
    except TypeError as ex:
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
        elif (estrategia == "c") or (estrategia == "A"):
            nodo = menor_valor()

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

def menor_valor():
    global frontera
    valor = (0, 0)
    for i in range(len(frontera)):
        n_valor = frontera[0].valor
        if n_valor < valor[0]:
            valor = (n_valor, i)
    
    n = frontera[valor[1]]
    frontera.remove(frontera[valor[1]])
    return n

def min_euclidea_objetivos(lista_n):
    global g
    dist_min = 0
    for i in range(len(lista_n)):
        for j in range(len(lista_n)):
            if i < j:
                d = lista_n[i].euclidea(lista_n[j])
                if (d < dist_min) or (dist_min == 0):
                    dist_min = d
    return dist_min

lista = ['1185', '1252', '1314']
n = "205"
nodo = g.lista_nodos.get(n)

nodo_arb = nodo_arbol(nodo, None)
e = estado (lista, nodo_arb, None)
nodo_arb.estado = e

if estrategia == "A":
    lista_n = []
    for nodo in lista:
        nodo_grafo = g.lista_nodos.get(nodo)   
        lista_n.append(nodo_grafo)
        
    d1 = min_euclidea_objetivos(lista_n)
    nodo_arb.heuri(d1)

frontera.append(nodo_arb)

if estrategia == "":
    raise Exception("Seleccione una estrategia")
    
algoritmoBusqueda()