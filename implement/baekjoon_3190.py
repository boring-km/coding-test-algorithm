from collections import deque

N = int(input())
board = [[0] * N for _ in range(N)]

K = int(input())
for i in range(K):
    apple = [int(i) for i in input().split()]
    board[apple[0]-1][apple[1]-1] = -1

L = int(input())
snake_moves = [0 for _ in range(10001)]
for i in range(L):
    move_time, direct = input().split()
    snake_moves[int(move_time)] = direct

moves = [[0, -1], [0, 1], [-1, 0], [1, 0]]  # 상 하 좌 우
time = 0
head = [0, 0]    # 현재 뱀 머리 위치 Y, X
snake = deque()
snake.append([0, 0])
board[0][0] = 1     # 처음 뱀 위치 초기화
head_dir = 3    # 머리의 이동 방향
while True:
    head[0] += moves[head_dir][1]
    head[1] += moves[head_dir][0]
    time += 1
    if head[0] < 0 or (N - 1) < head[0] or head[1] < 0 or (N - 1) < head[1]:
        break

    if board[head[0]][head[1]] == -1:
        board[head[0]][head[1]] = 1
        snake.append([head[0], head[1]])
    elif board[head[0]][head[1]] == 1:
        break
    else:
        board[head[0]][head[1]] = 1
        snake.append([head[0], head[1]])
        deleted = snake.popleft()
        board[deleted[0]][deleted[1]] = 0

    if snake_moves[time] == 'D':
        if head_dir == 3:
            head_dir = 1
        elif head_dir == 0:
            head_dir = 3
        elif head_dir == 1:
            head_dir = 2
        else:
            head_dir = 0
    if snake_moves[time] == 'L':
        if head_dir == 3:
            head_dir = 0
        elif head_dir == 0:
            head_dir = 2
        elif head_dir == 1:
            head_dir = 3
        else:
            head_dir = 1

print(time)