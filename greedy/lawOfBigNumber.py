# 23분 43초
N, M, K = [int(i) for i in input().split()]
array = [int(i) for i in input().split()]

array.sort(reverse=True)

result = 0
count = 0

for i in range(M):
    count += 1
    print(i, count)
    if K - count < 0:
        result += array[1]
        count = 0
        continue
    if K - count >= 0:
        result += array[0]

print(result)
