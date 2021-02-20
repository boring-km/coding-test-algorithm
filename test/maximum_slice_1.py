def solution(A):
    # write your code in Python 3.6
    n = len(A)
    if n == 3:
        return 0
    answer = 0
    head, tail = [0] * n, [0] * n

    for i in range(1, n-1):
        head[i] = max(0, head[i-1] + A[i])
    for i in range(n-2, 0, -1):
        tail[i] = max(0, tail[i+1] + A[i])

    for i in range(1, n-1):
        # head와 tail은 무조건 i-1, i+1로 두 칸 떨어져 있음
        answer = max(answer, head[i-1] + tail[i+1])

    return answer


print(solution([4,5,6,7]))