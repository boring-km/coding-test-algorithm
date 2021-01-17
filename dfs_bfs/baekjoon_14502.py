# 참조
# 예전에 풀었던 문제 복습
# https://lmcoa15.tistory.com/78
import sys
input = sys.stdin.readline

n, m = [int(i) for i in input().split()]

data, visited = [], []
wall_count = 0
ans = 0 # 바이러스가 최소로 퍼졌을 때의 값
virus_count = 0 # 바이러스가 퍼졌을 때의 값
x_mv = [0, 0, -1, 1]
y_mv = [1, -1, 0, 0]


def dfs_virus(y, x):
    global virus_count
    for i in range(4):
        ny = y+y_mv[i]
        nx = x+x_mv[i]

        if ny < 0 or ny >= n or nx < 0 or nx >= m:
            continue
        if data[ny][nx] == 1 or visited[ny][nx]:
            continue
        visited[ny][nx] += 1
        virus_count += 1
        dfs_virus(ny, nx)


def dfs_wall(count):
    global ans, visited, virus_count
    if count == 3:
        virus_count = 0
        visited = []
        for i in range(n):
            visited.append([0] * m)
        for i in range(n):
            for j in range(m):
                if data[i][j] == 2 and visited[i][j] == 0:
                    visited[i][j] = 1
                    virus_count += 1
                    dfs_virus(i,j)
        if ans == 0:
            ans = virus_count
        else:
            ans = min(ans, virus_count)
        return
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                dfs_wall(count + 1)
                data[i][j] = 0


for i in range(n):
    temp = [int(j) for j in input().split()]
    for j in range(len(temp)):
        if temp[j] == 1:
            wall_count += 1
    data.append(temp)

# DFS 시작!
dfs_wall(count=0)
# 전체 N X M 칸에서 기존 벽의 갯수 + 새로 설치할 3개의 벽 +
## 감염 이후의 바이러스 수를 빼면 안전한 영역만 남음
print((n*m) - (wall_count+3+ans))