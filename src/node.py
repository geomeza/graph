class Node:

    def __init__(self, index):
        self.index = index
        self.value = None
        self.neighbors = []

    def set_value(self, val):
        self.value = val

    def set_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)
        if self not in neighbor.neighbors:
            neighbor.neighbors.append(self)

    def find(self, val):
        if self.value == val:
            return self
        else:
            for neighbor in self.neighbors:
                neighbor.find(val)
        return None
