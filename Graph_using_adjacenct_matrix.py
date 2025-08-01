class Graph:
    def __init__(self,vno):
        self.vertex_count=vno
        self.adj_matrix=[[0]*vno for i in range(vno)]
    
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]=weight
            self.adj_matrix[v][u]=weight
        else:
            print("invalid vertex")
            
    def remove_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]=0
            self.adj_matrix[v][u]=0
        else:
            print("invalid matrix")
            
    def has_edge(self,u,v):
         if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
             return self.adj_matrix[u][v]!=0
         
    def print_adj_matrics(self):
        for row_list in self.adj_matrix:
            matrix=" ".join(map(str,row_list))
            print(matrix)
            
g=Graph(4)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,1)
g.print_adj_matrics()  
print(g.has_edge(2,3))    
g.remove_edge(1,2)    
        
            