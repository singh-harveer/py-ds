from collections import deque
from ds.graph import build
import math

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

def connectedComponentCount(graph):
    visited = set()
    count = 0
    for node in graph:
        if explore(graph, node, visited):
            count += 1
    
    return count


def explore(graph, current, visited):
    if current in visited:
        return False
    
    visited.add(current)
    
    for neighbor in graph[current]:
       explore(graph, neighbor, visited)
    
    return True

"""
count largest componet in given graph
if edges = e and nodes = n
we will be exploring all edge
so,
TC = O(e)
SC = O(n) # we might be storing all node in set or call stack
"""
def largestComponent(graph):
    maxSize = 0
    visited = set()
    for node in graph:
        currentSize = exploreSize(graph, node, visited)
        maxSize = max(maxSize, currentSize)
    
    return maxSize


def exploreSize(graph, current, visited):
    if current in visited:
        return 0
    visited.add(current)

    count = 1

    for neighbor in graph[current]:
        count += exploreSize(graph, neighbor, visited)
    
    return count


def shortestPath(edges, src, dst):
    graph = build(edges)
    visited = set()
    queue = deque([(src, 0)])

    while queue:
        current, distance = queue.popleft()

        if current == dst:
            return distance

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
    
    return -1


def islandCount(grid):
    visited = set()
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if exploreIsland(grid, r, c, visited):
                count += 1
    
    return count


def exploreIsland(grid, r, c, visited):
    rowInbound = 0 <= r and r < len(grid)
    colInbound = 0 <= c and c < len(grid[0])

    if not rowInbound or not colInbound:
        return False
    
    # check if current position is water
    if grid[r][c]=="W":
        return False
    
    # check if current position has been visited
    key = (r,c)
    if key in visited:
        return False
    visited.add(key)

    exploreIsland(grid, r-1, c, visited)
    exploreIsland(grid, r+1, c, visited)
    exploreIsland(grid, r, c-1, visited)
    exploreIsland(grid, r, c+1, visited)

    return True

def minIsLand(grid):
    visited = set()
    minCount = math.inf

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            currentCount = exploreMinIsland(grid, r, c, visited)
            if currentCount > 0:
                minCount = min(minCount, currentCount)
    
    return minCount


def exploreMinIsland(grid, r, c, visited):
    rowInbount = 0 <= r and r < len(grid)
    colInbound = 0 <= c and c < len(grid[0])

    if not rowInbount or not colInbound:
        return 0
    
    # now check current position if it is water.
    if grid[r][c] =="W":
        return 0
    
    key = (r,c)
    if key in visited:
        return 0
    visited.add(key)

    size = 1
    size += exploreMinIsland(grid, r-1, c, visited)
    size += exploreMinIsland(grid, r+1, c, visited)
    size += exploreMinIsland(grid, r, c-1, visited)
    size += exploreMinIsland(grid, r, c+1, visited)

    return size
    


        



