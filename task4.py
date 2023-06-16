import task1
import hashlib
import sys
from bisect import insort

g = task1.graph()
g.iniciar_grafo()
lista_nodos = g.lista_nodos
estados_visitados = []
frontera = []
estrategia = "" #p= profundidad, a = anchura, c = coste uniforme
maxdepth = -1
a = False
for i in range(len(sys.argv)):
    if sys.argv[i] == "-c":
        estrategia = "c"
    elif sys.argv[i] == "-p":
        estrategia = "p"
    elif sys.argv[i] == "-a":
        estrategia = "a"
    elif sys.argv[i] == "-A":
        estrategia = "A"
    elif sys.argv[i] == "-Ar":
        estrategia = "Ar"
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
    total_nodos = 0

    def __init__(self, nodo, padre):
        
        global estrategia
        global g
        self.id = nodo_arbol.total_nodos
        nodo_arbol.total_nodos += 1
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
            self.costo = float(self.padre.costo) + float(self.coste)
           
        if estrategia == "p":
            self.valor = 1/(self.profundidad + 1)
        elif estrategia == "a":
            self.valor = self.profundidad
        elif estrategia == "c":
            self.valor = self.costo
        elif estrategia == "A" or estrategia == "Ar":
            pass
        else:
            raise Exception("Escribe bien la estrategia")
    
    def heuri(self, heur):
        self.heuristica = heur
        self.valor = (self.costo + heur)

    def obtener_camino(self):
        # Crea una lista vacía para almacenar el camino
        camino = []
        nodo_final = self
        # Recorre los nodos desde el final hasta el inicial
        while nodo_final is not None:
            # Añade la información del nodo actual a la lista
            camino.append(nodo_final)

            # Avanza al nodo padre
            nodo_final = nodo_final.padre
  
        # Invertimos el orden de la lista para tener el camino en el orden correcto
        camino.reverse()
  
        # Concatena la información de todos los nodos en una cadena de texto
        cadena = ""
        for nodo in camino:
            # Si el nodo actual es objetivo y se encuentra en la lista de nodos objetivo, añade su información a la cadena
            try:
                estado = nodo.estado.id[(len(nodo.estado.id) -6): len(nodo.estado.id)]
                accion = "(" + str(nodo.padre.nodo_grafo.id) + "->" + str(nodo.nodo_grafo.id) + ")"
                cadena += "[" + str(nodo.id) + "][" + str(round(nodo.costo, 2)) + "," + "[" + nodo.estado.toString() + "|" + str(estado) + "]" + "," + str(nodo.padre.id) + "," + accion + "," + str(nodo.profundidad) + "," + str(round(nodo.heuristica, 2)) + "," + str(round(nodo.valor, 2)) + "]\n"
            except AttributeError:
                accion = None
                #[0][0.00,[(205,[1185,1252,1314])|bd1382],None,None,0,2191.98,2191.98]
                cadena += "[" + str(nodo.id) + "]" + str(round(nodo.costo, 2)) + ",[" + nodo.estado.toString() + "|" + str(estado) + "],None,None," + str(nodo.profundidad) + "," + str(round(nodo.heuristica, 2)) + "," + str(round(nodo.valor, 2)) + "]\n"
        print(cadena)

class estado:

    def __init__(self, lista_objetivos, current_nodo): #la lista de objetivos, el estado anterior, el nodo
        self.lista_objetivos = lista_objetivos
        self.current_nodo = current_nodo  # current_nodo y nodo_objetivo son el id del nodo
        self.cadena = "(" + self.current_nodo.nodo_grafo.id + ",("+ str(self.lista_objetivos) + "))"
        self.cadena=self.cadena.replace(" ","")
        self.id = hashlib.md5(self.cadena.encode("utf-8")).hexdigest() #Montamos cadena encriptada en md5, que será el id del estado
    
    def toString(self):
        return self.cadena

def min_euclideo(nodo, lista_objetivos):
    global g
    dist_min = float("inf")
    d = 0
    for objetivo in lista_objetivos:
        d = nodo.nodo_grafo.euclidea(g.lista_nodos.get(objetivo))
        if d < dist_min:
            dist_min = d
    return dist_min

def sucesor(nodo):
    global g
    global d1
    global arc_min_ec
    nodos = []
    global a
    e = nodo.estado
    
    try:
        
        adyacentes = g.adyacencia.get(str(nodo.nodo_grafo.id)) #Recogemos los nodos adyacentes del nodo actual
        for adyacente in adyacentes: # Por cada nodo adyacente
       
            n = g.lista_nodos.get(adyacente)
            n_arbol = nodo_arbol(n, nodo)
            
            if adyacente in e.lista_objetivos: # Si el adyacente esta en la lista de objetivos, le eliminamos de dicha lista
                l = e.lista_objetivos.copy()
                l.remove(adyacente)
                e2 = estado(l, n_arbol)# Creamos el siguiente estado, siendo el siguiente nodo, el nodo adyacente
            else:
                e2 = estado(e.lista_objetivos, n_arbol) # Creamos el siguiente estado, siendo el siguiente nodo, el nodo adyacente

            n_arbol.estado = e2

            if estrategia == "A":
                d2 = min_euclideo(n_arbol, e2.lista_objetivos)
                if d1 <= d2:
                    n_arbol.heuri(d1*len(e2.lista_objetivos)) 
                else:
                    n_arbol.heuri(d2*len(e2.lista_objetivos))
            elif estrategia == "Ar":
                n_arbol.heuri(arc_min_ec*len(e2.lista_objetivos)) 
            
            nodos.append(n_arbol)
            #Siguiente adyacente
        
    except TypeError as ex:
        pass
    
    return nodos

def algoritmoBusqueda(frontera, estados_visitados, maxdepth, estrategia):
    solucion = False
    nodo = ""
    
    while (len(frontera) != 0) and not solucion:

        if estrategia == "p":
            nodo = frontera.pop()
        elif (estrategia == "c") or (estrategia == "A" or (estrategia == "a") or (estrategia == "Ar")):
            nodo = frontera[0]
            frontera.remove(frontera[0])
        
        if len(nodo.estado.lista_objetivos) == 0:
            solucion = True
            nodo.obtener_camino()

        if (((nodo.profundidad <= maxdepth) or (maxdepth == -1)) & (nodo.estado.id not in estados_visitados)):
            estados_visitados.append(nodo.estado.id)
            expandir(nodo, frontera)

def expandir(nodo, frontera):
    nodos = sucesor(nodo)
    try:
        for nodo1 in nodos:
            insort(frontera, nodo1, key=lambda x: (x.valor, x.id))
            
    except TypeError:
        pass

def min_euclidea_objetivos(lista_n):
    dist_min = float("inf")
    for obj1 in lista_n:
        for obj2 in lista_n:
            if obj1 != obj2:
                d = obj1.euclidea(obj2)
                if d < dist_min:
                    dist_min = d
    return dist_min

lista = ['248', '528']
n = "37"
nodo = g.lista_nodos.get(n)
arc_min_ec = 0
nodo_arb = nodo_arbol(nodo, None)
e = estado(lista, nodo_arb)
nodo_arb.estado = e

if estrategia == "A":
    lista_n = []
    for nodo in lista:
        nodo_grafo = g.lista_nodos.get(nodo)   
        lista_n.append(nodo_grafo)
        
    d1 = min_euclidea_objetivos(lista_n) 
    nodo_arb.heuri(d1*len(lista))
elif estrategia == "Ar":
    min_coste = float("inf")
    h = 0
    for arista in g.graf:
        h = float(arista.length)
        if h < min_coste:
            min_coste = h
    min_coste = min_coste
    nodo_arb.heuri(min_coste*len(lista))
    arc_min_ec = min_coste
frontera.append(nodo_arb)

if estrategia == "":
    raise Exception("Seleccione una estrategia")
algoritmoBusqueda(frontera, estados_visitados, maxdepth, estrategia)