class Graph:
    def __init__(self, directed=False):
        self.nodes = {}
        self.directed = directed

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = []

    def add_edge(self, node1, node2):
        if node1 not in self.nodes:
            self.add_node(node1)
        if node2 not in self.nodes:
            self.add_node(node2)

        self.nodes[node1].append(node2)
        if not self.directed:
            self.nodes[node2].append(node1)


graph = Graph()

graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")


graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")


print("Graph:")
for node, neighbors in graph.nodes.items():
    print(f"{node}: {neighbors}")