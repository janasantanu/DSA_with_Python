class Graph:
    def __init__(self,vno):
        self.vertex_no=vno
        self.adjacency_list={v:[]for v in range(self.vertex_no)}
        
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_no and 0<=v<self.vertex_no:
            self.adjacency_list[u].append((v,weight))
            self.adjacency_list[v].append((u,weight))
        else:
            print("invalid vertex")
            
    def remove_edge(self,u,v):
        if 0<=u<self.vertex_no and 0<=v<self.vertex_no:
            self.adjacency_list[u]=[(vertex,weight)for vertex,weight in self.adjacency_list[u]if vertex!=v]
            self.adjacency_list[v]=[(vertex,weight)for vertex,weight in self.adjacency_list[v]if vertex!=u] 
        else:
            print("invalid vertex")
            
    def has_edge(self,u,v):
        if 0<=u<self.vertex_no and 0<=v<self.vertex_no:
            return any(vertex==v for vertex,w in self.adjacency_list[u])
        
        else:
            print("no edge")
    def print_adj_list(self):
        for vertex,n in self.adjacency_list.items():
            print("V",vertex,":",n)
            
g=Graph(6)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,5)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(3,4)
g.print_adj_list()