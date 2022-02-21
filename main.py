from ds import graph, graph_questions
from dp import dp_questions

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
    # g2 = {
    #     "f":["g", "i"],
    #     "g":["h"],
    #     "h":[],
    #     "i":["g", "k"],
    #     "j": ["i"],
    #     "k":[]
    # }
    # has path implementations
    # print(graph_questions.hasPath(g2, "f", "g"))
    # print(graph_questions.hasPathBFS(g2, "k", "g"))
    # build graph

    # edges = [
    #     ["i", "j"],
    #     ["k", "i"],
    #     ["m", "k"],
    #     ["k", "l"],
    #     ["o", "n"],
    # ]

    # result = graph.build(edges)
    # print(result)
    # result = graph_questions.UndirectedPath(edges, "i", "k") #True
    # print(result)

    # gg = {
    #     3:[],
    #     4:[6],
    #     6:[4,5,7,8],
    #     8:[6],
    #     7:[6],
    #     5:[6],
    #     1:[2],
    #     2:[1]
    # }

    # result = graph_questions.connectedComponentCount(gg)
    # print(result)

    # gg1 = {
    #     0:[8,1,5],
    #     1:[0],
    #     5:[0,8],
    #     8:[0,5],
    #     2:[3,4],
    #     3:[2,4],
    #     4:[3,2]
    # }

    # result = graph_questions.largestComponent(gg1)
    # print(result)


    # edges = [
    #     ["w", "x"],
    #     ["x", "y"],
    #     ["z", "y"],
    #     ["z", "v"],
    #     ["w", "v"],
    # ]
    # result = graph_questions.shortestPath(edges, "w", "z")
    # print(result)

    # grid = [
    #     ["W", "L", "W", "W", "W"],
    #     ["W", "L", "W", "W", "W"],
    #     ["W", "W", "W", "L", "W"],
    #     ["W", "L", "L", "W", "W"],
    #     ["L", "W", "W", "L", "L"],
    #     ["L", "L", "W", "W", "W"],
    # ]

    # result = graph_questions.islandCount(grid)
    # print(result)
    # minSize = graph_questions.minIsLand(grid)
    # print(minSize)

    # print(dp_questions.fibMemoization(7))
    # print(dp_questions.fibMemoization(50))

    # print(dp_questions.fibUsingTabulation(7))
    # print(dp_questions.fibUsingTabulation(50))

    # print(dp_questions.knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    # print(dp_questions.knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    # print(dp_questions.knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    # print(dp_questions.canSumMemoization(700, [2,3,5,8]))
    # print(dp_questions.canSumMemoization(2, [6,3,4,8]))
    # print(dp_questions.canSumTabulation(700, [2,3,5,8]))
    # print(dp_questions.canSumTabulation(2, [6,3,4,8]))
    print(dp_questions.howSumMemoization(5, [2,3,5,8]))
    print(dp_questions.howSumMemoization(1111, [5,5,5,5]))





