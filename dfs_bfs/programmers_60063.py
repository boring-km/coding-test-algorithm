from collections import deque


def bfs(board, n):
    qx = deque([1])
    qy = deque([0])
    qa = deque([3])  # 로봇의 현재 방향
    visited = [[False] * n for _ in range(n)]
    # [y, x]
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]]   # 0, 1, 2, 3

    while qy and qx:
        y, x, a = qy.popleft(), qx.popleft(), qa.popleft()
        for i in range(4):
            if a == i:
                move_to(board, i, move, n, qx, qy, qa, visited, x, y)
            else:
                ty, tx = y, x
                if a == 0 and i == 2:
                    ty, tx = y + 1, x - 1
                if a == 0 and i == 3:
                    ty, tx = y + 1, x + 1

                if a == 1 and i == 2:
                    ty, tx = y - 1, x - 1
                if a == 1 and i == 3:
                    ty, tx = y - 1, x + 1

                if a == 2 and i == 0:
                    ty, tx = y - 1, x + 1
                if a == 2 and i == 1:
                    ty, tx = y + 1, x + 1

                if a == 3 and i == 0:
                    ty, tx = y - 1, x - 1
                if a == 3 and i == 1:
                    ty, tx = y + 1, x - 1

                if 0 <= ty < n and 0 <= tx < n:
                    if board[ty][tx] <= 0:
                        move_to(board, i, move, n, qx, qy, qa, visited, x, y)
        for i in range(n):
            print(board[i])
        print("------")
    return board[n-1][n-1]


def move_to(board, i, move, n, qx, qy, qa, visited, x, y):
    my, mx = y + move[i][0], x + move[i][1]
    if 0 <= my < n and 0 <= mx < n:
        if board[my][mx] != 1 and not visited[my][mx]:
            qx.append(mx)
            qy.append(my)
            qa.append(i)
            visited[y][x] = True
            visited[my][mx] = True
            board[my][mx] = board[y][x] - 1


def solution(board):
    answer = bfs(board, len(board))
    return answer


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))