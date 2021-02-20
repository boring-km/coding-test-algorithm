# 바로 통과~
def solution(A):
    n = len(A)
    if n == 0:
        return 0

    cur = A[0]
    answer = 0
    for i in range(1, n):
        if A[i] - cur > answer:
            answer = A[i] - cur
        else:
            cur = min(cur, A[i])

    return answer


print(solution([23171, 21011, 21123, 21366, 21013, 21367]))