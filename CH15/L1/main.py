class Graph:
    def breadth_first_search(self, v):
        visited_vertices = []
        to_visit = []

        to_visit.append(v)

        while(len(to_visit) != 0):
            vertex = to_visit.pop(0)
            visited_vertices.append(vertex)
            sorted_neighbor_list = sorted(self.graph.get(vertex))
            for n in sorted_neighbor_list:
                if(visited_vertices.count(n) == 0 and to_visit.count(n) == 0):
                    to_visit.append(n)

        return visited_vertices

# En resumen se van apilando en el queue(to_visit) y despues en el visited. Si es letra lo hace en orden alfabetico las visitas garantizando orden.
# Este es el wide




        

    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result

