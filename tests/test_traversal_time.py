import sys
sys.path.append('analysis')

from railroad_travel_time import traversal_time_without_tree,traverse_with_tree

real_results = [['A', 'B', 'D', 'C', 'E', 'F', 'G'], ['D', 'A', 'E', 'B', 'C', 'F', 'G']]

railroad_segments = [('B','C'), ('B','A'), ('A','D'), ('E','D'), ('C','F'), ('G','C')]

starting_towns = ['A', 'D']

for i in range(len(real_results)):
    with_tree = traverse_with_tree(railroad_segments, starting_towns[i])
    without_tree = traversal_time_without_tree(railroad_segments, starting_towns[i])
    print('---------------------------------')
    print('TRAVERSAL TEST WITH TREE:', i+1)
    assert with_tree == real_results[i], ('Traversal With Tree Incorrect, Should be', real_results[i], 'got', with_tree)
    print('Passed')
    print('---------------------------------')
    print('TRAVERSAL TEST WITHOUT TREE:', i+1)
    assert without_tree == real_results[i], ('Traversal Without Tree Incorrect, Should be', real_results[i], 'got', without_tree)
    print('Passed')
