import sys
sys.path.append('src')
from directed_graph import DirectedGraph

edges = [(0,1),(1,2),(3,1),(4,3),(1,4),(4,5),(3,6)]
directed_graph = DirectedGraph(edges)

arr = [[child.indx for child in node.children] for node in directed_graph.nodes]
assert arr == [[1], [2,4], [], [1,6], [3,5], [], []], 'Wrong array'
arr = [[parent.indx for parent in node.parents] for node in directed_graph.nodes]
assert arr == [[], [0,3], [1], [4], [1], [4], [3]], 'Weong Array'

assert directed_graph.calc_distance(0,3) == 3, 'Wrong distance'
assert directed_graph.calc_distance(3,5) == 3, 'Wrong distance'
assert directed_graph.calc_distance(0,5) == 3, 'Wrong distance'
assert directed_graph.calc_distance(4,1) == 2, 'Wrong distance'
assert directed_graph.calc_distance(2,4) == False, 'Wrong distance'

assert directed_graph.find_path(0,3) == [0, 1, 4, 3], 'wrong Path'
assert directed_graph.find_path(3,5) == [3, 1, 4, 5], 'wrong Path'
assert directed_graph.find_path(0,5) == [0, 1, 4, 5], 'wrong Path'
assert directed_graph.find_path(4,1) == [4, 3, 1], 'wrong Path'
assert directed_graph.find_path(2,4) == False, 'wrong Path'
print('All tests passed')