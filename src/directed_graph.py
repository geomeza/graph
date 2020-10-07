from directed_node import DirectedNode

class DirectedGraph:

    def __init__(self, edges, vertices = None):
        self.edges = edges
        self.vertices = vertices
        self.nodes = []
        self.build_from_edges()

    def build_from_edges(self):
        vertices = []
        for edge in self.edges:
            if edge[0] not in vertices:
                vertices.append(edge[0])
                self.nodes.append(DirectedNode(edge[0]))
            if edge[1] not in vertices:
                vertices.append(edge[1])
                self.nodes.append(DirectedNode(edge[1]))
        for edge in self.edges:
            parent = edge[0]
            child = edge[1]
            self.nodes[parent].add_child(self.nodes[child])
            self.nodes[child].add_parent(self.nodes[parent])
        self.vertices = vertices

    def find_path(self, starter, ender):
        return self.nodes[starter].find(self.nodes[ender])
    
    def breadth_first(self, starter):
        q = [self.nodes[starter]]
        result = []
        while len(result) < len(self.nodes):
            for node in q:
                if node not in result:
                    result.append(node)
                for child in node.children:
                    if child not in result and child not in q:
                        q.append(child)
                        result.append(child)
                q.remove(node)
        return [node.indx for node in result]

    def calc_distance(self, starter, ender):
        if self.nodes[starter].children == []:
            return False
        else:
            return len(self.find_path(starter, ender)) - 1

    def find_path(self, starter, ender):
        all_paths = [[starter]]
        result = [starter]
        q = [starter]
        if self.nodes[starter].children == []:
            return False
        else:
            while ender not in q:
                for node in q:
                    for child in self.nodes[node].children:
                        if child.indx not in result and child.indx not in q:
                            q.append(child.indx)
                            result.append(child.indx)
                            for path in all_paths:
                                parents = [parent.indx for parent in child.parents]
                                if child.indx not in path and path[-1] in parents:
                                    copy = path[:]
                                    copy.append(child.indx)
                                    all_paths.append(copy)
                    q.remove(node)
                for path in all_paths:
                    if ender in path:
                        return path
                            

edges = [(0,1),(1,2),(3,1),(4,3),(1,4),(4,5),(3,6)]
directed_graph = DirectedGraph(edges)

print(directed_graph.calc_distance(0,3))

# print([[child.index for child in node.children] for node in directed_graph.nodes])

# print(directed_graph.find_path(0,5))
# print(directed_graph.nodes[0].find(3))