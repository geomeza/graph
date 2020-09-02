from node import Node

class Graph:

    def __init__(self, edges, vertices):
        self.edges = edges
        self.vertices = vertices
        self.nodes = [Node(i) for i in range(len(vertices))]
        for i in range(len(self.nodes)):
            self.nodes[i].set_value(self.vertices[i])
        self.build_from_edges(edges)

    def build_from_edges(self, edges):
        for node in self.nodes:
            for edge in self.edges:
                if node.index == edge[0]:
                    for other_node in self.nodes:
                        if other_node.index == edge[1]:
                            node.set_neighbor(other_node)
                if node.index == edge[1]:
                    for other_node in self.nodes:
                        if other_node.index == edge[0]:
                            node.set_neighbor(other_node)

    def depth_first_search(self, node_index, result = [], starter = None):
        node = self.nodes[node_index]
        if len(result) == 0:
            starter = node
        result.append(node_index)
        for neigbor in node.neighbors:
            if neigbor.index not in result:
                self.depth_first_search(neigbor.index, result = result, starter = starter)
        if node == starter:
            return result

    def breadth_first_search(self, starting_index):
        q = [starting_index]
        result = []
        while len(q) > 0:
            visited = []
            for i in range(len(q)):
                for edge in self.edges:
                    if edge[0] == q[i] and edge[1] not in result:
                        q.append(edge[1])
                    if edge[1] == q[i] and edge[0] not in result:
                        q.append(edge[0])
                visited.append(q[i])
            for nodes in visited:
                q.remove(nodes)
                if nodes not in result:
                    result.append(nodes)
        return result

    def find_distance(self, start_node, end_node):
        generation_counter = 0
        q = [start_node]
        result = []
        while len(q) > 0:
            if end_node in q:
                return generation_counter
            visited = []
            for i in range(len(q)):
                for edge in self.edges:
                    if edge[0] == q[i] and edge[1] not in result:
                        q.append(edge[1])
                    if edge[1] == q[i] and edge[0] not in result:
                        q.append(edge[0])
                visited.append(q[i])
            for nodes in visited:
                q.remove(nodes)
                if nodes not in result:
                    result.append(nodes)
            generation_counter += 1
