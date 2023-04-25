class Graph:
    # vertices_list = [v1,v2,v3,...,vn]
    # edges_list = [(v1,v2),(v2,v3),...,(vi,vj)]
    def __init__(self,vertices_list,edges_list):
        self.vertices_list = vertices_list
        self.edges_list = edges_list
        self.arr = [[] for _ in range(len(vertices_list))]
        
        for vertex in self.arr:

    
mi_grafo = Graph([1,2,3],[(1,2),(1,3),(2,3)])
print(mi_grafo.arr)


