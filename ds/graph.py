from collections import deque

def depthFirstTraversalInterative(graph, source):
    stack = [source]

    while stack:
        current = stack.pop()
        print(current)

        for neighbor in graph[current]:
            stack.append(neighbor)

def depthFirstTraversalRecursive(graph, source):
    print(source)
    for neighbor in graph[source]:
        depthFirstTraversalRecursive(graph, neighbor)

'''breath search can only be implemented using itervative method
  we can not do it using recursive
'''
def breathFirstTraversal(graph, source):
    queue = deque([source])

    while queue:
        current = queue.popleft()
        print(current)

        for neighbor in graph[current]:
            queue.append(neighbor)


def build(edges):
    graph = {}

    for edge in edges:
        a = edge[0]
        b = edge[1]

        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        
        graph[a].append(b)
        graph[b].append(a)
    
    return graph
    



