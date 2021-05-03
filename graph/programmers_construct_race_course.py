from collections import deque


def solution(board):
    n = len(board)

    def bfs(start_move):
        record = [[1e9 for _ in range(n)] for _ in range(n)]
        move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        q = deque([0, 0, 0, start_move])
        record[0][0] = 0
        while q:
            y, x, cost, before = q.popleft()
            for i in range(4):
                ty = y + move[i][0]
                tx = x + move[i][1]
                if i != before:
                    temp = cost + 600
                else:
                    temp = cost + 100
                if 0 <= ty < n and 0 <= tx < n and board[ty][tx] == 0 and record[ty][tx] > temp:
                    record[ty][tx] = temp
                    q.append([ty, tx, temp, i])
        return record[n-1][n-1]
    # 하단으로 먼저 진행, 우측으로 먼저 진행
    return min(bfs(0), bfs(1))


print(solution([[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 1], [0, 0, 0, 0]]))
# print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
