#!/usr/bin/python
import xml.sax
import math
from sortedcontainers import *

graphCR = []
nodos = []
list_graph_CR = {}
list_nodos = SortedDict()


class Nodes:

    def __init__( self,id ):
        self.id= id     #node identifier
        self.osmid_original=""  #different node attributes d4-d11
        self.y=""
        self.x=""
        self.street_count=""
        self.longitude=""
        self.latitude=""
        self.ref=""
        self.highway=""      

    def euclidea(self, n):

        dist = math.sqrt((float(self.x) - float(n.x))**2 + (float(self.y) - float(n.y))**2)
        return dist
        
class Edges:

    def __init__( self,source,target,id ):
        self.source= source  #source -> target
        self.target= target
        self.id = id
        self.osmid=""       #different edge attributes d12-d27
        self.highway=""
        self.junction=""
        self.oneway=""
        self.reversed=""
        self.length=""
        self.geometry=""
        self.u_original=""
        self.v_original=""
        self.speed_kph=""
        self.ref=""
        self.name=""
        self.bridge=""
        self.lanes=""
        self.maxspeed=""
        self.tunnel=""

class Handler(xml.sax.ContentHandler):
    
    def __init__(self):
        self.node=""
        self.edge=""
        self.data=""
        self.CurrentData=""
        self.DataKey=""
    
    def startElement(self, tag, attrs):

        self.CurrentData=tag

        if tag=="node":      #indicates which node is being parsed
            self.node=Nodes(attrs["id"])
        
        elif tag=="edge":      #indicates which edge is being parsed
            self.edge=Edges((attrs["source"]),(attrs["target"]),(attrs["id"]))

        elif tag=="data":       #for parsing the data
            self.DataKey=attrs["key"]

    def characters(self, content):
        if self.CurrentData=="data":
            self.data=content

    def endElement(self, name):
        if self.CurrentData=="data":
                
            #node data
            if self.DataKey=="d4":
                self.node.osmid_original=self.data
            elif self.DataKey=="d5":
                self.node.y=self.data
            elif self.DataKey=="d6":
                self.node.x=self.data
            elif self.DataKey=="d7":
                self.node.street_count=self.data
            elif self.DataKey=="d8":
                self.node.longitude=self.data
            elif self.DataKey=="d9":
                self.node.latitude=self.data
            elif self.DataKey=="d10":
                self.node.ref=self.data
            elif self.DataKey=="d11":
                self.node.highway=self.data
            #edge data
            elif self.DataKey=="d12":
                self.edge.osmid=self.data
            elif self.DataKey=="d13":
                self.edge.highway=self.data
            elif self.DataKey=="d14":
                self.edge.junction=self.data
            elif self.DataKey=="d15":
                self.edge.oneway=self.data
            elif self.DataKey=="d16":
                self.edge.reversed=self.data
            elif self.DataKey=="d17":
                self.edge.length=self.data
            elif self.DataKey=="d18":
                self.edge.geometry=self.data
            elif self.DataKey=="d19":
                self.edge.u_original=self.data
            elif self.DataKey=="d20":
                self.edge.v_original=self.data
            elif self.DataKey=="d21":
                self.edge.speed_kph=self.data
            elif self.DataKey=="d22":
                self.edge.ref=self.data
            elif self.DataKey=="d23":
                self.edge.name=self.data
            elif self.DataKey=="d24":
                self.edge.bridge=self.data
            elif self.DataKey=="d25":
                self.edge.lanes=self.data
            elif self.DataKey=="d26":
                self.edge.maxspeed=self.data
            elif self.DataKey=="d27":
                self.edge.tunnel=self.data
            
        elif name=="node":
            nodos.append(self.node)

            a = self.node        #adding edges to the sorted list
            if self.node.id in list_nodos:
                list_nodos.setdefault(self.node.id, a)
            else:
                list_nodos[self.node.id] = a

        elif name=="edge":
            
            if self.edge.id == "0":
                
                graphCR.append(self.edge)
                a = []        #adding edges to the sorted list
                if self.edge.source in list_graph_CR:
                    a = list_graph_CR.get(self.edge.source)
                    a.append(self.edge.target)
                    a = sorted(a, key=int)
                    list_graph_CR[self.edge.source] = a
                else:
                    list_graph_CR[self.edge.source] = [self.edge.target]
    
        self.CurrentData=""
    
class graph:

    def __init__(self):

        self.graf= graphCR
        self.nodos = nodos
        self.adyacencia = list_graph_CR
        self.lista_nodos = list_nodos
        
    def iniciar_grafo(self):
        HANDLER = Handler()
        parser=xml.sax.make_parser() #reader of xml
        parser.setContentHandler(HANDLER) #setting the content handler
        parser.parse("graph.xml") #xml where graph is described

    def get_arista(self, source, target):
        
        for arista in self.graf:
           if (arista.source == source) & (arista.target == target):
                return arista