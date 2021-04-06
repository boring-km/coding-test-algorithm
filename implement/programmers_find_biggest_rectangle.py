def solution(board):
    for row in board: # 정답의 최소값이 0인지 1인지 먼저 판별
        if sum(row):
            answer = 1
            break
    else:
        return 0
    # 1행 1열부터 board를 2x2 정사각형으로 탐색하면서 우측 아래 값 최신화
    # 어차피 값이 1이면 true, 0이면 false
    row_size = len(board)
    col_size = len(board[0])
    for i in range(1, row_size):
        for j in range(1, col_size):
            if board[i-1][j-1] and board[i-1][j] and board[i][j-1] and board[i][j]:
                # 정사각형의 크기를 board에 저장
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
                answer = max(answer, board[i][j] ** 2)
    return answer


print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))

"""
처음 board
0 1 1 1
1 1 1 1
1 1 1 1
0 0 1 0

최종 board
0 1 1 1
1 1 2 2
1 2 2 3
0 0 1 0
"""