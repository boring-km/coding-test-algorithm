def solution(board, moves):
    answer = 0
    n = len(board)
    basket = []
    move_size = len(moves)
    for i in range(move_size):
        move = moves[i] - 1
        for j in range(n):
            target = board[j][move]
            if target != 0:
                board[j][move] = 0
                if len(basket) > 0:
                    if basket[-1] == target:
                        answer += 2
                        basket.pop()
                        break
                basket.append(target)
                break
    print(basket)
    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 1, 4]))
