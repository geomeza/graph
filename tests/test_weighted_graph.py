from weighted_graph import WeightedGraph
import sys
sys.path.append('src')

weights = {
    (0, 1): 3,
    (1, 7): 4,
    (7, 2): 2,
    (2, 5): 1,
    (5, 6): 8,
    (0, 3): 2,
    (3, 2): 6,
    (3, 4): 1,
    (4, 8): 8,
    (8, 0): 4
}

vertex_values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
weighted_graph = WeightedGraph(weights, vertex_values)

dist = weighted_graph.calc_distance(8, 4)

assert dist == 7, ('WRONG DIST:', dist, 'SHOULD BE 7')

assert [weighted_graph.calc_distance(8, n) for n in range(9)] == [4, 7, 12, 6, 7, 13, 21, 11, 0], ('WRONG VALUES:',
                                                                                                   [weighted_graph.calc_distance(8, n) for n in range(9)], 'SHOULD BE [4, 7, 12, 6, 7, 13, 21, 11, 0]')


assert weighted_graph.calc_shortest_path(8, 4) == [8, 0, 3, 4], 'BRUH'

assert weighted_graph.calc_shortest_path(8, 7) == [8, 0, 1, 7], 'SECOND BRUH'

assert weighted_graph.calc_shortest_path(
    8, 6) == [8, 0, 3, 2, 5, 6], 'THIRD BRUH'
