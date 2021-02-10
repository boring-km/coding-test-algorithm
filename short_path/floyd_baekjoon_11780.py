import sys
input = sys.stdin.readline
n, m = int(input()), int(input())
data = [[1e9] * (n+1) for _ in range(n+1)]
data_route = [[[] for __ in range(n + 1)] for _ in range(n + 1)]

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            data[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if data[a][b] != 0:
        data[a][b] = min(data[a][b], c)
    else:
        data[a][b] = c
    data_route[a][b] = [a, b]

for _ in range(n+1):
    print(data_route[_])

# 플로이드
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            pre = data[a][b]
            new = data[a][k] + data[k][b]
            if new < pre:
                data[a][b] = new
                # 새로운 경로를 추가
                data_route[a][b] = data_route[a][k] + data_route[k][b][1:]


for i in range(1, n+1):
    for j in data[i][1:]:
        if j == 1e9:
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()

for i in range(1, n+1):
    for j in range(1, n+1):
        answer = data_route[i][j]
        if len(answer) == 0:
            print(0)
        else:
            print(len(answer), end=' ')
            for k in range(len(answer)):
                print(answer[k], end=' ')
            print()
