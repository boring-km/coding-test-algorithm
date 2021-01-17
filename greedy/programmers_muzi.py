# 포기

def solution(food_times, k):

    size = len(food_times)
    cycle = k // size
    final_move = k % size
    if final_move == 0:
        final_move = size
    check = [False] * size
    k -= size * cycle

    if cycle == min(food_times):
        for i in range(size):
            if food_times[i] == cycle and i < final_move:
                k += 1
                check[i] = False
    elif cycle > min(food_times):
        print('예외')
    else:
        print('정상')

    if k+1 > size:
        return 1
    else:
        return k+1


print(solution([2, 412, 2], 6))

# 2 1 8
# 2 0 8
# 2 0 7
# 1 0 7
# 1 0 6