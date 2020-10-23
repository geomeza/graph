import sys
sys.path.append('src')
from graph import Graph

def assertion(graph, indexes, node_values, node_neighbor_lengths):
    print('--------------')
    print('Index Test')
    assert [node.index for node in graph.nodes] == indexes, ('Indexes are wrong')
    print('Passed')
    print('--------------')
    print('Values Test')
    assert [node.value for node in graph.nodes] == node_values, ('Node Values are wrong')
    print('Passed')
    print('--------------')
    print('Neighbor Lengths Test')
    assert [len(node.neighbors) for node in graph.nodes] == node_neighbor_lengths, ('Node Neighbor Lengths are wrong')
    print('Passed')
    print('--------------')

def distance_assertion(graph, distance, starter, ender):
    dist = graph.find_distance(starter, ender)
    assert dist == distance, ('Wrong Distance got',dist,'Should have been', distance)
    print('Passed')

def path_assertion(graph, path, starter, ender):
    graph_path = graph.find_path(starter, ender)
    assert path == graph_path, 'Wrong Paths'
    print('\nPassed')

edges = [(0,1),(1,2),(1,3),(3,4),(1,4),(4,5)]
vertices = ['a','b','c','d','e','f']
graph = Graph(edges, vertices)

# assertion(graph, [0, 1, 2, 3, 4, 5], ['a','b','c','d','e', 'f'], [1, 4, 1, 2, 3, 1])

pairs = [[0, 4], [5, 2], [0, 5], [4, 1], [3, 3]]
distances = [2, 3, 3, 1, 0]
paths = [[0, 1, 4], [5, 4, 1, 2], [0, 1, 4, 5], [4, 1], [3]]

edges = [(0,1),(1,2),(1,3),(3,4),(1,4),(4,5)]
vertices = ['a','b','c','d','e','f']
graph = Graph(edges, vertices)

print(graph.breadth_first_search(2))

# for i in range(len(distances)):
#     print('\n-------------------')
#     print('Distance Test', i+1, ':')
#     distance_assertion(graph, distances[i], pairs[i][0], pairs[i][1])
#     print('-------------------')
# for i in range(len(paths)):
#     print('\n---------------------')
#     print('Path Test',i+1,':')
#     path_assertion(graph, paths[i], pairs[i][0], pairs[i][1])
#     print('\n---------------------')

