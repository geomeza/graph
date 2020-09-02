class Tree:
    def __init__(self, head = None):
        if head is not None:
            self.root = Node(head)
        else:
            self.root = None
        self.breadth = []

    def append(self, value):
        current_node = self.root
        child = Node(value)
        while current_node.children_are_filled():
            current_node = current_node.get_next_node_across_layer()

        current_node.children.append(child)
        child.parent = current_node

    def build_from_edges(self,edges):
        edge_parents = []
        edge_children = []
        union = []
        for edge in edges:
            edge_parents.append(edge[0])
            edge_children.append(edge[1])
        for parents in edge_parents:     
            if parents not in edge_children:
                self.root = Node(parents)
        union = (set(edge_parents) | set(edge_children))
        node_union = []
        for elem in union:
            node_union.append(Node(elem))
        for nodes in node_union:
            nodes.children = []
            if nodes.data == self.root.data:
                self.root = nodes
            for edge in edges:
                if edge[0] == nodes.data:
                    for more_nodes in node_union:
                        if edge[1] == more_nodes.data:
                            nodes.children.append(more_nodes)

    def get_node(self,current_node, node_to_find):
        if current_node.data == node_to_find:
            return current_node
        else: 
            for child in node.children:
                search = self.get_node(current_node = chil, node_to_find = node_to_find)
                if search is not None:
                    return search
            return None

    def insert_tree(self, new_tree, node):
        finder = self.get_node(self.root, node)
        finder.children.append(new_tree.root)

    def breadth_first(self, q = [], iter = 0, result = []):
        if iter == 0:
            q = [self.root]
        removers = []
        while len(q) > 0:
            before_length = len(q)
            for i in range(len(q)):
                removers.append(q[i])
                self.breadth.append(q[i].data)
                for children in q[i].children:
                    q.append(children)
            for elem in removers:
                q.remove(elem)
            iter += 1
            self.breadth_first(q,iter,result)

    def show_breadth_first(self):
        self.breadth_first()
        return self.breadth

    def show_depth_first(self, current_node):
        print(current_node.data)
        for child in current_node.children:
            self.show_depth_first(child)

class Node:
    def __init__(self, value):
        self.data = value
        self.parent = None
        self.children = []

    def append_child(self, val):
        child = Node(val)
        child.parent = self
        self.children.append(child)

    def children_are_filled(self):
        return len(self.children) == 2

    def look_for_node(self, value):
        if self.data == value:
            return self
        else:
            for child in self.children:
                if child.look_for_node(value) is not None:
                    return child.look_for_node(value)
            return None

    def get_next_node_across_layer(self):
        parent = self.parent
        if parent is None:
            return self.children[0]
        elif self == parent.children[0]:
            return parent.children[1]
        elif self == parent.children[1]:
            return parent.get_next_node_across_layer().children[0]

# edges_B = [('a','b'),('b','c'),('c','d'),('b','e'),('b','f'),('f','g')]
# tree_B = Tree()
# tree_B.build_from_edges(edges_B)
# tree_B.show_depth_first(tree_B.root)
