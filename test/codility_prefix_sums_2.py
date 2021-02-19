def solution(S, P, Q):
    M = len(P)
    N = len(S)
    A = [[0, 0, 0, 0]]
    counter = [0] * 4
    result = []
    for i in S:
        if i == "A":
            counter[0] += 1
            A.append(counter[:])
        elif i == "C":
            counter[1] += 1
            A.append(counter[:])
        elif i == "G":
            counter[2] += 1
            A.append(counter[:])
        elif i == "T":
            counter[3] += 1
            A.append(counter[:])

    for i in range(M):
        for j in range(4):
            val = A[Q[i]+1][j] - A[P[i]][j]
            if val != 0:
                result.append(j + 1)
                break

    return result


print(solution('TC', [0, 0, 1], [0, 1, 1]))
