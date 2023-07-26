import numpy as np
import sys
sys.stdin = open('87694_input.txt', 'r')


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    xmax = 0
    ymax = 0
    # make a load

    def make_load(G, p1, p2, type: int):
        x1, y1 = p1
        x2, y2 = p2
        sx, bx = min(x1, x2), max(x1, x2)
        sy, by = min(y1, y2), max(y1, y2)

        for i in range(sx, bx+1):
            G[i][sy] += type
            G[i][by] += type
        for j in range(sy, by+1):
            G[sx][j] += type
            G[bx][j] += type

        G[x1][y1] -= type
        G[x2][y1] -= type
        G[x1][y2] -= type
        G[x2][y2] -= type

    def delete_load(G, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        sx, bx = min(x1, x2), max(x1, x2)
        sy, by = min(y1, y2), max(y1, y2)

        for i in range(sx+1, bx):
            for j in range(sy+1, by):
                G[i][j] = 0
                G[i][j] = 0

    def print_graph(G):
        ret = np.array(G)
        print(np.rot90(ret, 1))
    # make a Graph
    for (x1, y1, x2, y2) in rectangle:
        xmax = max(xmax, x1, x2)
        ymax = max(ymax, y1, y2)
    graph = [[0 for i in range(ymax+1)]for j in range(xmax+1)]

    print("before")
    print_graph(graph)

    for i, (x1, y1, x2, y2) in enumerate(rectangle):
        make_load(graph, (x1, y1), (x2, y2), i+1)
        print("after making load")
        print_graph(graph)
    for (x1, y1, x2, y2) in rectangle:
        delete_load(graph, (x1, y1), (x2, y2))
        print("after deleting load")
        print_graph(graph)

    return answer


# print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [
#       4, 3, 6, 9], [2, 6, 8, 8]],	1,	3,	7,	8))  # 17
# print(solution([[1, 1, 8, 4], [2, 2, 4, 9], [
#       3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1))  # 11
# print(solution([[1, 1, 5, 7]], 1, 1, 4, 7))  # 9
print(solution([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10))  # 15
# print(solution([[2,2,5,5],[1,3,6,4],[3,1,4,6]]	,1	,4	,6	,3 ))# 10
