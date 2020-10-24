# 37분 29초
from collections import deque

n, m = [int(i) for i in input().split()]
data = [input() for j in range(n)]
visited = [[False for i in range(m)] for j in range(n)]
moveY = [1, -1, 0, 0]
moveX = [0, 0, -1, 1]
result = 0


def bfs(graph, startY, startX, visited):
    queueY = deque([startY])
    queueX = deque([startX])
    visited[startY][startX] = True

    while queueY or queueX:
        ty = queueY.popleft()
        tx = queueX.popleft()
        for i in range(4):
            targetX = tx + moveX[i]
            targetY = ty + moveY[i]
            if 0 <= targetX < m and 0 <= targetY < n:
                if graph[targetY][targetX] == '0' and not visited[targetY][targetX]:
                    queueY.append(targetY)
                    queueX.append(targetX)
                    visited[targetY][targetX] = True


for y in range(n):
    for x in range(m):
        if visited[y][x]:
            continue
        if not visited[y][x] and data[y][x] == '0':
            bfs(data, y, x, visited)
            result += 1

print(result)
# 테스트
# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111
