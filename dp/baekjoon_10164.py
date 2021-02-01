import copy
n, m, k = map(int, input().split())

robotY, robotX = k // m, k % m
print(robotY, robotX)
# robotY = 1, robotX = 3
# n = 2, m = 4
# 0,0 -> 1, 2
# 1,2 ->


def dfs(x, y, limit_x, limit_y, visit):
    if (x < limit_x and y <= limit_y) or (x <= limit_x and y < limit_y):
        if not visit[y][x]:
            visit[y][x] = True
            return dfs(x+1, y, limit_x, limit_y, copy.deepcopy(visit)) + dfs(x, y+1, limit_x, limit_y, copy.deepcopy(visit))
        else:
            return 0
    elif x == limit_x and y == limit_y:
        return 1
    else:
        return 0


if k != 0:
    first = dfs(0, 0, robotX-1, robotY, [[False] * m for _ in range(n)])
    second = dfs(0, 0, m-robotX, n-1-robotY, [[False] * m for _ in range(n)])
    print(first * second)
else:
    print(dfs(0, 0, m-1, n-1, [[False] * m for _ in range(n)]))

