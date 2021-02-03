n, m, k = map(int, input().split())

robotY, robotX = k // m, k % m
if k == 0:
    robotX, robotY = m, n-1
else:
    if robotX == 0:
        robotY -= 1
        robotX = m

dp = [[0] * robotX for _ in range(robotY+1)]    # dfs를 반복문으로?
dp2 = [[0] * (m-robotX+1) for _ in range(n-robotY)]

dp[0][0] = 1
dp2[0][0] = 1
if robotX == 0 or robotY == 0:
    dp[robotY][robotX-1] = 1
for i in range(robotY):
    for j in range(robotX):
        if j+1 < robotX and i <= robotY:
            dp[i][j+1] = dp[i][j] + dp[i-1][j+1]
        if j < robotX and i+1 <= robotY:
            dp[i+1][j] = dp[i][j] + dp[i+1][j-1]
if k != 0:
    if n - robotY - 1 == 0 or m - robotX + 1 == 0:
        dp2[n-robotY-1][m-robotX] = 1
    for i in range(n-robotY-1):
        for j in range(m-robotX+1):
            if j+1 < m-robotX+1 and i <= n-robotY-1:
                dp2[i][j+1] = dp2[i][j] + dp2[i-1][j+1]
            if j < m-robotX+1 and i+1 <= n-robotY-1:
                dp2[i+1][j] = dp2[i][j] + dp2[i+1][j-1]
    print(dp[robotY][robotX-1] * dp2[n-robotY-1][m-robotX])
else:
    print(dp[robotY][robotX-1])

# print(dp)
# print(dp[robotY][robotX-1])
# print(dp2)
# print(dp2[n-robotY-1][m-robotX])



# def find_load(x, y, limit_x, limit_y, visit):
#     if (x < limit_x and y <= limit_y) or (x <= limit_x and y < limit_y):
#         if not visit[y][x]:
#             visit[y][x] = True
#             return find_load(x+1, y, limit_x, limit_y, copy.deepcopy(visit)) + find_load(x, y+1, limit_x, limit_y, copy.deepcopy(visit))
#         else:
#             return 0
#     elif x == limit_x and y == limit_y:
#         return 1
#     else:
#         return 0
#
#
# if k != 0:
#     first = find_load(0, 0, robotX-1, robotY, [[False] * robotX for _ in range(robotY+1)])
#     second = find_load(0, 0, m-robotX, n-1-robotY, [[False] * (m-robotX+1) for _ in range(n-robotY)])
#     print(first * second)
# else:
#     print(dfs(0, 0, m-1, n-1, [[False] * m for _ in range(n)]))
#
# end_time = time.time()

# print("time:", end_time-start_time)
