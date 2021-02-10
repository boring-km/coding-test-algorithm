from collections import deque
n = int(input())
space = []
shark_start = []
move = [[0, -1], [-1, 0], [0, 1], [1, 0]]
shark_size = 2
eat_count = 0
answer = 0
for i in range(n):
    temp = [int(_) for _ in input().split()]
    space.append(temp)
    for j, shark in enumerate(temp):
        if shark == 9:
            shark_start = [i, j]
            space[i][j] = 0


def bfs(start, visit):
    global eat_count, shark_size, shark_start
    queue_x = deque([start[1]])
    queue_y = deque([start[0]])
    sx, sy = start[1], start[0]
    visit[sy][sx] = 1
    while queue_x or queue_y:
        tx = queue_x.popleft()
        ty = queue_y.popleft()
        for g in range(4):
            x, y = move[g][1] + tx, move[g][0] + ty
            if 0 <= x < n and 0 <= y < n:   # 공간에서 벗어나지 않으면
                if shark_size < space[y][x]:    # 더 큰 물고기가 있는 칸은 지나가지 못함
                    continue
                if visit[y][x] >= 1:
                    continue
                queue_x.append(x)
                queue_y.append(y)
                visit[y][x] = visit[ty][tx] + 1  # 방문만 하기
                if 0 < space[y][x] < shark_size:    # 먹을 수 있는 물고기가 있다면
                    eat_count += 1
                    if eat_count == shark_size:
                        shark_size += 1
                        eat_count = 0
                    space[y][x] = 0
                    shark_start = [y, x]
                    return visit[y][x] - 1, False
    return 0, True     # 탐색을 끝까지 했지만 먹을 수 있는 물고기가 없었다면


while True:
    temp_visit = [[0] * n for _ in range(n)]
    temp_count, is_end = bfs(shark_start, temp_visit)
    answer += temp_count
    if is_end:
        break

print(answer)
