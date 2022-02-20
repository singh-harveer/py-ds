from ds import graph, graph_questions
if __name__ =="__main__":

    g = {
        "a":["b", "c"],
        "b":["d"],
        "c":["e"],
        "d":["f"],
        "e": [],
        "f":[]
    }
    # graph.depthFirstTraversalInterative(g, "a")
    # print("------------------------------")
    # graph.depthFirstTraversalRecursive(g, "a")
    g2 = {
        "f":["g", "i"],
        "g":["h"],
        "h":[],
        "i":["g", "k"],
        "j": ["i"],
        "k":[]
    }
    # has path implementations
    # print(graph_questions.hasPath(g2, "f", "g"))
    # print(graph_questions.hasPathBFS(g2, "k", "g"))
    # build graph

    edges = [
        ["i", "j"],
        ["k", "i"],
        ["m", "k"],
        ["k", "l"],
        ["o", "n"],
    ]

    # result = graph.build(edges)
    # print(result)
    result = graph_questions.UndirectedPath(edges, "i", "k") #True
    print(result)




