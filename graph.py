class Graph:
    def __init__(self) -> None:
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, v1, v2, is_directed=False):
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.graph[v1].append(v2)
        if not is_directed:
            self.graph[v2].append(v1)

    def display(self):
        for key, value in self.graph.items():
            print(f"{key} === {value}")

    def get_vertices(self):  # To get only the vertices
        print(list(self.graph.keys()))
        return

    def get_edges(self):  # To get all the edges
        for key, value in self.graph.items():
            for v in value:
                print(f"({key}, {v})", end=" ")

    def remove_vertices(self, v):
        if v in self.graph:
            del self.graph[v]
        for val in self.graph.values():
            if v in val:
                val.remove(v)

    def is_edge(self, v1, v2):
        return v1 in self.graph[v2] or v2 in self.graph[v1]

    def remove_edge(self, v1, v2):
        if self.is_edge(v1, v2):
            self.graph[v1].remove(v2)
            self.graph[v2].remove(v1)

    def DFS_traversal(self, start, alreadyvisited=set()):
        if start not in alreadyvisited:
            alreadyvisited.add(start)
            print(start, end=" ")

            for child in self.graph[start]:
                self.DFS_traversal(child, alreadyvisited)
                


    def BFS_traversal(self, start):
        alreadyvisited = {start}
        q = [start]

        while len(q) > 0:
            current = q.pop(0)
            print(current, end=" ")
            for child in self.graph[current]:
                if child not in alreadyvisited:
                    alreadyvisited.add(child)
                    q.append(child)
                    


    def shortest_path(self, start, end):
        alreadyvisited = {start}
        q = [(start, [start])]

        while len(q) > 0:
            curr, path = q.pop(0)
            for child in self.graph[curr]:
                if child not in alreadyvisited:
                    if child == end:
                        return path + [child]
                    q.append((child, path + [child]))
                    alreadyvisited.add(child)


graph = Graph()
graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("C", "D")
graph.add_edge("D", "E")
graph.add_edge("A", "F")
graph.add_edge("B", "F")
graph.add_edge("C", "F")
graph.add_edge("D", "F")
graph.add_edge("E", "F")
print()
graph.BFS_traversal("A")
print()
print(graph.shortest_path("A", "E"))
