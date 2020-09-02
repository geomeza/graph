import sys
sys.path.append('src')

from tree import Tree

def change_root(edges, desired_root):
    for i in range(len(edges)):
        if edges[i][1] == desired_root:
            edges[i] = (edges[i][1],edges[i][0])
    complete = 0
    while complete < len(edges):
        for i,j in edges:
            if i!= desired_root:
                for x,y in edges:
                    if i==y:
                        complete+=1
                        break
                else:
                    complete = 0
                    index = edges.index((i,j))
                    edges[index] = (edges[index][1],edges[index][0])
    return edges

def traversal_time_without_tree(edges, starting_town):
    travels_q = [starting_town]
    result = []
    while len(travels_q) > 0:
        traveled = []
        for i in range(len(travels_q)):
            for edge in edges:
                if edge[0] == travels_q[i] and edge[1] not in result:
                    travels_q.append(edge[1])
                if edge[1] == travels_q[i] and edge[0] not in result:
                    travels_q.append(edge[0])
            traveled.append(travels_q[i])
        for t in traveled:
            travels_q.remove(t)
            result.append(t)
    return result

def traverse_with_tree(edges, starting_town):
    modified = change_root(edges, starting_town)
    town = Tree()
    town.build_from_edges(modified)
    return town.show_breadth_first()