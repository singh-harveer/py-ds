from collections import deque
from ds.graph import build

'''
Check if there is path between given source and destination.
nodes = n
edges = e
time = O(e)
space :O(n)
'''

# has path using depth first traversal
def hasPath(graph, source, dest):
    if source == dest:
        return True

    stack = [source]
    while stack:
        for neighbor in graph[source]:
            if hasPath(graph, neighbor, dest):
                return True
        
    return False

def hasPathBFS(graph, source, dest):
    queue = deque([source])

    while queue:
        current = queue.popleft()

        if current == dest:
            return True
        
        for neighbor in graph[current]:
            queue.append(neighbor)

    return False

def UndirectedPath(edges, source, dest):
    graph = build(edges)
    visited = set()
    return hasUndirectedpath(graph, source, dest, visited)


def hasUndirectedpath(graph, source, dest, visited):
    if source in visited:
        return False

    # add current node to visited
    visited.add(source)

    if source == dest:
        return True
    
    for neighbor in graph[source]:
        if hasUndirectedpath(graph, neighbor, dest, visited):
            return True
    
    return False


