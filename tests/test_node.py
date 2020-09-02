import sys
sys.path.append('src')
from node import Node


def assertion(node, index=None, value=None, neighbors=None):
    if index is not None:
        assert node.index == index, ('Index is wrong, got', node.index, 'should be', index)
        print('\nINDEX TEST PASSED')
    if value is not None:
        assert node.value == value, ('Node Value is wrong, got', node.value, 'should be', value)
        print('\nVALUE TEST PASSED')
    if neighbors is not None:
        assert node.neighbors == neighbors, ('Neighbords are wrong, got', node.neighbors, 'should be', neighbors)
        print('\nNEIGHBORS TEST PASSED')

print('------------------------------------')
print('String Node tests')
string_node = Node(0)
string_node.set_value('asdf')
assertion(string_node, 0, 'asdf', [])
print('------------------------------------')

print('------------------------------------')
print('\nNumeric Node Tests')
numeric_node = Node(1)
numeric_node.set_value(765)
numeric_node.set_neighbor(string_node)
assertion(numeric_node, 1, 765, [string_node])
print('------------------------------------')

print('------------------------------------')
print('Neighbor Test for string_node')
assertion(string_node, neighbors = [numeric_node])
print('------------------------------------')

print('------------------------------------')
print('Array Node Tests')
array_node = Node(2)
array_node.set_value([[1,2],[3,4]])
array_node.set_neighbor(numeric_node)
assertion(array_node, 2, [[1,2],[3,4]], [numeric_node])
print('------------------------------------')

print('------------------------------------')
print('Numeric Node Neighbors Test')
assertion(numeric_node, neighbors = [string_node, array_node])
print('------------------------------------')