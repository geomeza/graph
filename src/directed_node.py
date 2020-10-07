class DirectedNode:

    def __init__(self, index):
        self.indx = index
        self.value = None
        self.parents = []
        self.children = []

    def set_value(self, val):
        self.value = val

    def add_child(self, child):
        if child not in self.children:
            self.children.append(child)

    def add_parent(self, parent):
        if parent not in self.parents:
            self.parents.append(parent)  
