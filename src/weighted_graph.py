from weighted_node import WeightedNode

class WeightedGraph:

    def __init__(self, weights, vertex_values):
        self.weights = weights
        self.vertex_values = vertex_values
        self.nodes = self.make_nodes(self.weights)

    def make_nodes(self, weights):
        nodes = []
        for edge, weight in weights.items():
            indices = [node.index for node in nodes]
            node_one_weights = {key:val for key,val in weights.items() if edge[0] in key}
            node_two_weights = {key:val for key,val in weights.items() if edge[1] in key}
            if edge[0] not in indices:
                node = WeightedNode(edge[0], self.vertex_values[edge[0]], node_one_weights)
                nodes.append(node)
            if edge[1] not in indices:
                node = WeightedNode(edge[1], self.vertex_values[edge[1]], node_two_weights)
                nodes.append(node)
        return nodes

    def find_node(self, index):
        for node in self.nodes:
            if node.index == index:
                return node

    def calc_distance(self, starting_node, ending_node, current = None, visited = []):
        if current is None:
            current = self.find_node(starting_node)
            current.d_val = 0
        for edge, weight in current.weights.items():
            neighbor = self.find_node(edge[edge.index(current.index) - 1])
            if neighbor.d_val > current.d_val + weight:
                neighbor.d_val = current.d_val + weight
                if neighbor in visited:
                    visited.remove(neighbor)
        if current not in visited:
            visited.append(current)
            for edge in current.weights.keys():
                neighbor = self.find_node(edge[edge.index(current.index) - 1])
                self.calc_distance(starting_node, ending_node, current = neighbor, visited = visited)
        if len(visited) == len(self.nodes):
            ender = self.find_node(ending_node)
            return ender.d_val
