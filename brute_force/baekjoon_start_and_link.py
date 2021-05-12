from itertools import combinations


answer = 1e9
n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    temp = input().split()
    for j in range(n):
        board[i][j] = int(temp[j])

comb = list(combinations(range(n), n // 2))
for first in comb:
    second = []
    for i in range(n):
        if i not in first:
            second.append(i)

    first_comb = list(combinations(first, 2))
    second_comb = list(combinations(second, 2))
    a, b = 0, 0
    for i in range(len(first_comb)):
        f = first_comb[i]
        s = second_comb[i]
        a += board[f[0]][f[1]] + board[f[1]][f[0]]
        b += board[s[0]][s[1]] + board[s[1]][s[0]]
    answer = min(answer, abs(a-b))

print(answer)


