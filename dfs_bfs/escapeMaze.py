# 30분 29초
from collections import deque

n, m = [int(i) for i in input().split()]
data = [input() for _ in range(n)]
visited = [[0 for i in range(m)] for j in range(n)]
moveY = [1, -1, 0, 0]
moveX = [0, 0, -1, 1]


def bfs(graph, y, x, visited):

    queueY = deque([y])
    queueX = deque([x])
    visited[y][x] = 1

    while queueY or queueX:
        ty = queueY.popleft()
        tx = queueX.popleft()

        for i in range(4):
            tempY = ty + moveY[i]
            tempX = tx + moveX[i]
            if 0 <= tempY < n and 0 <= tempX < m:
                if graph[tempY][tempX] == '1' and visited[tempY][tempX] == 0:
                    queueY.append(tempY)
                    queueX.append(tempX)
                    visited[tempY][tempX] += visited[ty][tx] + 1
    return visited[n-1][m-1]


print(bfs(data, 0, 0, visited))
