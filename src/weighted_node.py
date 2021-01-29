class WeightedNode:

    def __init__(self, index, value, weights):
        self.index = index
        self.value = value
        self.weights = weights
        self.d_val = 9999999
        self.path = []