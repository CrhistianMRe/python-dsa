class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if(self.graph.get(u) == None):
            self.graph[u] = set()
        if(self.graph.get(v) == None):
            self.graph[v] = set()
        self.graph.get(u).add(v)
        self.graph.get(v).add(u)
            

    # don't touch below this line

    def edge_exists(self, u, v):
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) and (u in self.graph[v])
        return False

