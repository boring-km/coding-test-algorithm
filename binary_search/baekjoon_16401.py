# 13분 정도
m, n = map(int, input().split())
snacks = [int(i) for i in input().split()]

left, right = 1, max(snacks)
answer = 0
while right - left >= 0:
    mid = (left + right) // 2
    check = 0
    for i in range(n):
        if mid <= snacks[i]:
            check += snacks[i] // mid
    if check >= m:
        answer = max(answer, mid)
        left = mid + 1
    else:
        right = mid - 1

print(answer)
