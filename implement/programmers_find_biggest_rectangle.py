def solution(board):
    answer = 0
    row = len(board)
    col = len(board[0])


    def find(x, y):
        size = 1
        while y+size < row and x+size < col:
            for i in range(y, y+size+1):
                for j in range(x, x+size+1):
                    if board[i][j] == 0:
                        return size
            size += 1
        return size

    for y in range(row):
        for x in range(col):
            if board[y][x] == 1:
                result = find(x, y)
                answer = max(answer, result*result)

    return answer


print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))