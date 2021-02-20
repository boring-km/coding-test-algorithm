def solution(A):
    N = len(A)
    test = []
    for i in range(N):
        test.append([A[i], i])
    test.sort(reverse=True)

    answer = 0

    for i in range(N-1):
        size, pos = test[i][0], test[i][1]
        front, back = pos - size, pos + size
        for j in range(i+1, N):
            child_size, child_pos = test[j][0], test[j][1]
            child_front, child_back = child_pos - child_size, child_pos + child_size
            # 자식 원이 왼쪽으로 튀어 나올 때, 붙어있을 때,
            # 자식 원이 오른쪽으로 튀어 나올 때, 붙어있을 때
            # 자식 원이 안에 있을 때
            if child_front <= front <= child_back \
                    or child_front <= back <= child_back \
                    or front <= child_front and child_back <= back:
                answer += 1
            if answer > 10000000:
                return -1

    return answer


print(solution([1, 5, 2, 1, 4, 0]))
