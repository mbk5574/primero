#!/usr/bin/python
import xml.sax

graphCR = []

# graph attributes d0-d3
class Graph:

    def _init_( self,edgedefault ):
        self.edgedefault= edgedefault #graph type
        self.created_date= ""
        self.created_with= ""
        self.crs= ""
        self.simplified= ""

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

class Edges:

    def _init_(self,source,target):
        self.source=source  #source -> target
        self.target=target
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

class GraphHandler(xml.sax.ContentHandler):
    
    def _init_(self):
        self.graph=""
        self.node=""
        self.edge=""
        self.data=""
        self.CurrentData=""
        self.DataKey=""
    
    def startElement(self, tag, attrs):

        self.CurrentData=tag

        if tag=="graph":
            self.graph=Graph(attrs["edgedefault"])
            print("Graph:", self.graph.edgedefault)

        elif tag=="node":      #indicates which node is being parsed
            self.node=Nodes(attrs["id"])
            print ("Node:", self.node.id)
        
        elif tag=="edge":      #indicates which edge is being parsed
            self.edge=Edges(attrs["source"],attrs["target"])
            print ("Edge: -Source[", self.edge.source,"], -Target[", self.edge.target,"]")

        elif tag=="data":       #for parsing the data
            self.DataKey=attrs["key"]

    def characters(self, content):
        if self.CurrentData=="data":
            self.data=content

    def endElement(self, name):
        if self.CurrentData=="data":

            #graph data

            if self.DataKey=="d0":
                self.graph.created_date=self.data
                print ("Created date: ", self.graph.created_date)
            elif self.DataKey=="d1":
                self.graph.created_with=self.data
                print("Created with: ", self.graph.created_with)
            elif self.DataKey=="d2":
                self.graph.crs=self.data
            elif self.DataKey=="d3":
                self.graph.simplified==self.data
            

            #falta los datos de los nodos d4-d11


            #falta los datos de las aristas d12-d27

            #si lo completais haced los comentarios en ingles, lo que falta es igual a
            #lo ultimo escrito
            
            

