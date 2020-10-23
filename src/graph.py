from node import Node

class Graph:

    def __init__(self, edges, vertices):
        self.edges = edges
        self.vertices = vertices
        self.nodes = [Node(i) for i in range(len(vertices))]
        for i in range(len(self.nodes)):
            self.nodes[i].set_value(self.vertices[i])
        self.build_from_edges(edges)

    # def build_from_edges(self, edges):
    #     for node in self.nodes:
    #         for edge in self.edges:
    #             if node.index == edge[0]:
    #                 for other_node in self.nodes:
    #                     if other_node.index == edge[1]:
    #                         node.set_neighbor(other_node)
    #             if node.index == edge[1]:
    #                 for other_node in self.nodes:
    #                     if other_node.index == edge[0]:
    #                         node.set_neighbor(other_node)

    def build_from_edges(self, edges):
        for edge in edges:
            node = self.nodes[edge[0]]
            other_node = self.nodes[edge[1]]
            if other_node not in node.neighbors:
                node.set_neighbor(other_node)
            if node not in other_node.neighbors:
                other_node.set_neighbor(node)

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

    def breadth_first_search(self,starter):
        result = []
        q = [starter]
        while len(result) < len(self.nodes):
            for node in q:
                if node not in result:
                    result.append(node)
                for neighbor in self.nodes[node].neighbors:
                    if neighbor.index not in result and neighbor.index not in q:     
                        q.append(neighbor.index)
                        result.append(neighbor.index)
                q.remove(node)
        return result

    def find_distance(self, starter, goal):
        generation_counter = 0
        result = [starter]
        queue = [starter]
        while goal not in result:
            result_prior = [elem for elem in result]
            for node in queue:
                if node not in result:
                    result.append(node)
                for neighbor in self.nodes[node].neighbors:
                    if neighbor.index not in result and neighbor.index not in queue:     
                        queue.append(neighbor.index)
                        result.append(neighbor.index)
                queue.remove(node)
            if result_prior != result:
                generation_counter += 1
        return generation_counter

    def find_path(self,starter, goal):
        all_paths = [[starter]]
        result = []
        queue = [starter]
        while goal not in queue:
            for node in queue:
                for neighbor in self.nodes[node].neighbors:
                    if neighbor.index not in result and neighbor.index not in queue:
                        queue.append(neighbor.index)
                        result.append(neighbor.index)
                        for path in all_paths:
                            node_neigbors = [node.index for node in self.nodes[neighbor.index].neighbors]
                            if neighbor.index not in path and path[-1] in node_neigbors:
                                copy = path[:]
                                copy.append(neighbor.index)
                                all_paths.append(copy)
                queue.remove(node)
            for path in all_paths:
                if goal in path:
                    return path
        return queue
