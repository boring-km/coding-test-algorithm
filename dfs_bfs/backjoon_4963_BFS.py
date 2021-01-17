import sys
from collections import deque
input = sys.stdin.readline

moveY = [1, -1, 0, 0, 1, 1, -1, -1]
moveX = [0, 0, -1, 1, 1, -1, -1, 1]


def bfs(graph, startY, startX, visited):
    queueY = deque([startY])
    queueX = deque([startX])
    visited[startY][startX] = True

    while queueY or queueX:
        ty = queueY.popleft()
        tx = queueX.popleft()
        for i in range(8):
            targetX = tx + moveX[i]
            targetY = ty + moveY[i]
            if 0 <= targetX < m and 0 <= targetY < n:
                if graph[targetY][targetX] == 1 and not visited[targetY][targetX]:
                    queueY.append(targetY)
                    queueX.append(targetX)
                    visited[targetY][targetX] = True

resultList = []
while True:
    temp = input().split()
    m, n = [int(i) for i in temp]
    if n == 0 and m == 0:
        break
    data = [[int(i) for i in input().split()] for j in range(n)]
    visited = [[False for i in range(m)] for j in range(n)]
    result = 0

    for y in range(n):
        for x in range(m):
            if visited[y][x]:
                continue
            if not visited[y][x] and data[y][x] == 1:
                bfs(data, y, x, visited)
                result += 1
    resultList.append(result)

for item in resultList:
    print(item)


