

def solution(grid):
    answer = []

    # 초기화
    h = len(grid)
    w = len(grid[0])
    visited = [[[False] * 4 for _ in range(w)] for _ in range(h)]

    # 하, 좌, 상, 우
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    def move(data, a, b, c):
        y = a
        x = b
        way = c
        count = 0
        while not visited[y][x][way]:
            count += 1
            visited[y][x][way] = True
            if data[y][x] == 'L':
                # 임계영역: 아래로 가다가 왼쪽으로 틀면 오른쪽
                way = 3 if way == 0 else way - 1
            elif data[y][x] == 'R':
                # 임계영역: 오른쪽으로 가다가 오른쪽으로 가면 아래
                way = 0 if way == 3 else way + 1
            else:
                # 방향 그대로
                way = way
            # (현재 좌표 + 이동한 거리 + 길이)를 길이로 나눈 나머지
            y = (y + dy[way] + h) % h
            x = (x + dx[way] + w) % w
        return count

    for i in range(h):
        for j in range(w):
            for k in range(4):
                if not visited[i][j][k]:
                    answer.append(move(grid, i, j, k))

    return sorted(answer)


print(solution(['SL', 'LR']))
