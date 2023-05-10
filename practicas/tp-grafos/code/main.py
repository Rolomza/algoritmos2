import dictionary
import math
import copy

class Vertex:
    def __init__(self,key):
        self.key = key
    color = None
    parent = None
    distance = None
    f = None

class Graph:
    # vertices_list = [v1,v2,v3,...,vn]
    # edges_list = [(v1,v2),(v2,v3),...,(vi,vj)]
    def __init__(self,vertices_list,edges_list):
        self.vertices_list = vertices_list
        self.edges_list = edges_list
    
        self.adj_list = [[] for _ in range(len(self.vertices_list))]
        
        for i in range(len(edges_list)):
            self.adj_list[edges_list[i][0].key - 1].append(edges_list[i][1])
            self.adj_list[edges_list[i][1].key - 1].append(edges_list[i][0])

    # Parte 1

    def exist_path(self,v1,v2):
        if v1 not in self.vertices_list or v2 not in self.vertices_list:
            return 'Error: v1 or v2 not belong to graph'
        if v1 in self.adj_list[v2-1] and v2 in self.adj_list[v1-1]:
            return True
        return False
    
    def is_connected(self):
        newG = copy.deepcopy(self)
        BFS(newG,v1)
        for vertex in newG.vertices_list:
            if vertex.color == 'white':
                return False
        return True
    
    def is_tree(self):
        # Un arbol es un grafo de n vertices, aciclico con n-1 aristas
        # Verifico cantidad de aristas
        if len(self.vertices_list) - 1 != len(self.edges_list):
            return False
        
        # Detecto si existen ciclos en el grafo
        visited = set()
        start_vertex = self.vertices_list[0]
        stack = [(start_vertex,None)]
        while stack != []:
            current_vertex, parent = stack.pop()
            visited.add(current_vertex)
            for adj_vertex in self.adj_list[current_vertex.key-1]:
                if adj_vertex != parent:
                    if adj_vertex not in visited:
                        stack.append((adj_vertex,current_vertex)) # Ciclo detectado, el grafo no es un arbol
                    else:
                        return False
        
        # Reviso si hay vertices no visitados (componentes desconectadas)
        if len(visited) != len(self.vertices_list):
            return False

        # Si se cumplen con todas las condiciones, el grafo es un arbol
        return True
    
    def is_complete(self):
        vertices_count = len(self.vertices_list)
        if len(self.edges_list) != vertices_count * ((vertices_count - 1) / 2):
            return False
        return True
    
    def convert_tree(self):
        removal_list = []
        visited = set()
        start_vertex = self.vertices_list[0]

        self.dfs_convert_tree(start_vertex,visited,None,removal_list)
        
        return removal_list
    
    def dfs_convert_tree(self, vertex, visited, parent, removal_list):
            visited.add(vertex)
            for neighbor in self.adj_list[vertex.key - 1]:
                print('vertex:',vertex.key,'neighbor',neighbor.key)
                if neighbor not in visited:
                    self.dfs_convert_tree(neighbor, visited, vertex, removal_list)
                elif neighbor != parent:
                    removal_list.append([vertex.key, neighbor.key])
    
    # Parte 2

    class DisjointSet:
        def __init__(self):
            self.head = None
            self.tail = None

    class SetElement:
        def __init__(self,set_member):
            self.set_member = set_member
            self.next = None
            self.set_object = None

    def count_connections(self):
        collection = {}
        i = 1
        for vertex in self.vertices_list:
            collection[i] = {vertex.key}
            i += 1

        print(collection)
        for edge in self.edges_list:
            u = edge[0].key
            v = edge[1].key
            print(u,v)

        for subset in collection:
            print()
                # print('u esta en collection',collection[u])
                # collection[u] = collection[u].union(collection[v])
                # collection.pop(v)

        #print(collection)

    def draw_graph(self):
        for i in range(len(self.adj_list)):
            print('|',i+1,'|-->',end="")
            for vertex in self.adj_list[i]:
                print('|',vertex.key,'|',end="")
            print()


def BFS(G,s):
    for vertex in G.vertices_list:
        if vertex.key != s.key:
            vertex.color = 'white'
            vertex.distance = math.inf
    s.color = 'gray'
    s.distance = 0
    Q = []
    Q.insert(0,s)
    while Q != []:
        u = Q.pop()
        for vertex in G.adj_list[u.key-1]:
            if vertex.color == 'white':
                vertex.color = 'gray'
                vertex.distance = u.distance + 1
                vertex.parent = u
                Q.insert(0,vertex)
        u.color = 'black'

def DFS(G):
    for vertex in G.vertices_list:
        vertex.color = 'white'
    global time
    time = 0
    for vertex in G.vertices_list:
        if vertex.color == 'white':
            DFS_visit(G,vertex)

def DFS_visit(G,u):
    global time
    time += 1
    u.distance = time
    u.color = 'gray'

    #print(f"vertex: {u.key} (Start time: {u.distance})")

    for vertex in G.adj_list[u.key-1]:
        if vertex.color == 'white':
            vertex.parent = u
            DFS_visit(G,vertex)
    
    u.color = 'black'
    time += 1
    u.f = time

    #print(f"vertex: {u.key} (Finish time: {u.f})")


v1 = Vertex(1)
v2 = Vertex(2)
v3 = Vertex(3)
v4 = Vertex(4)
v5 = Vertex(5)
v6 = Vertex(6)
v7 = Vertex(7)
v8 = Vertex(8)
v9 = Vertex(9)
v10 = Vertex(10)
vertices = [v1,v2,v3,v4,v5,v6,v7,v8,v9,v10]
edges = [(v1,v2),(v1,v3),(v2,v3),(v2,v4),(v5,v6),(v5,v7),(v8,v9)]
mi_grafo = Graph(vertices,edges)
mi_grafo.draw_graph()
print(mi_grafo.count_connections())


