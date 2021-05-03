from collections import deque


def solution(board):
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    start = [0, 0]
    q = deque([start])
    record = deque([[]])
    n = len(board)
    answer = 500 * n * n

    dest = [n - 1, n - 1]
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[0][0] = True

    while q:
        cur = q.popleft()
        before = record.popleft()

        if cur[:] == dest[:]:
            answer = min(answer, board[n-1][n-1])
        for i in range(4):
            ty = cur[0] + move[i][0]
            tx = cur[1] + move[i][1]
            if cur[0] == 3 and cur[1] == 1:
                print()

            if 0 <= ty < n and 0 <= tx < n and board[ty][tx] != 1 and (not visited[ty][tx] or board[cur[0]][cur[1]] + 100 <= board[ty][tx]):
                prev = board[cur[0]][cur[1]]
                visited[ty][tx] = True
                # 같은 방향
                if not before:
                    board[ty][tx] += 100
                elif before[0] == before[2]:  # 좌 or 우
                    if before[3] - before[1] > 0:  # 우측
                        if i == 0:  # 우측
                            if board[ty][tx] != 0:
                                board[ty][tx] = min(prev + 100, board[ty][tx])
                            else:
                                board[ty][tx] = prev + 100
                        else:  # 우측이 아님
                            if board[ty][tx] == 0:
                                board[ty][tx] = prev + 600
                            else:
                                board[ty][tx] = min(prev + 600, board[ty][tx])
                    else:
                        if i == 2:  # 좌측
                            if board[ty][tx] != 0:
                                board[ty][tx] = min(prev + 100, board[ty][tx])
                            else:
                                board[ty][tx] = prev + 100
                        else:  # 좌측이 아님
                            if board[ty][tx] == 0:
                                board[ty][tx] = prev + 600
                            else:
                                board[ty][tx] = min(prev + 600, board[ty][tx])
                else:
                    if before[2] - before[0] > 0:  # 하단
                        if i == 1:
                            if board[ty][tx] != 0:
                                board[ty][tx] = min(prev + 100, board[ty][tx])
                            else:
                                board[ty][tx] = prev + 100
                        else:  # 우측이 아님
                            if board[ty][tx] == 0:
                                board[ty][tx] = prev + 600
                            else:
                                board[ty][tx] = min(prev + 600, board[ty][tx])
                    else:
                        if i == 3:
                            if board[ty][tx] != 0:
                                board[ty][tx] = min(prev + 100, board[ty][tx])
                            else:
                                board[ty][tx] = prev + 100
                        else:  # 우측이 아님
                            if board[ty][tx] == 0:
                                board[ty][tx] = prev + 600
                            else:
                                board[ty][tx] = min(prev + 600, board[ty][tx])
                # 다른 방향
                q.append([ty, tx])
                record.append([cur[0], cur[1], ty, tx])
    for i in range(n):
        print(board[i])
    return answer


print(solution([[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 1], [0, 0, 0, 0]]))
# print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
