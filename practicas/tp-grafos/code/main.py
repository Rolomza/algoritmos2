import dictionary

class Graph:
    # vertices_list = [v1,v2,v3,...,vn]
    # edges_list = [(v1,v2),(v2,v3),...,(vi,vj)]
    def __init__(self,vertices_list,edges_list):
        self.vertices_list = vertices_list
        self.edges_list = edges_list
        hash_function = lambda vertex: vertex - 1

        self.arr = dictionary.Dictionary(len(vertices_list),hash_function)
        
        for edge in edges_list:
            self.arr.insert(edge[0],edge[1])
            self.arr.insert(edge[1],edge[0])

vertices = [1,2,3,4,5,6]
edges = [(1,4),(1,3),(1,2),(2,3),(2,6)]
mi_grafo = Graph(vertices,edges)
print(mi_grafo.arr.table)


