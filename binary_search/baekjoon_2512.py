# 15분 정도
n = int(input())
array = [int(i) for i in input().split()]
m = int(input())

left, right = 1, m
answer = 0

while right - left >= 0:
    mid = (left + right) // 2
    check = []
    for i in range(n):
        if array[i] <= mid:
            check.append(array[i])
        else:
            check.append(mid)
    if sum(check) > m:
        right = mid - 1
    elif sum(check) < m:
        answer = max(answer, max(check))
        left = mid + 1
    else:
        answer = max(check)
        break

print(answer)
