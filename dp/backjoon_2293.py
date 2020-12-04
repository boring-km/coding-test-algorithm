# n 시간 ㅠㅠ
n, k = map(int, input().split())
data = [0] * 101
for i in range(1, n+1):
    data[i] = int(input())

cur = [0] * 10001
cur[0] = 1

for i in range(1, n+1):
    for j in range(1, k+1):
        if j >= data[i]:
            cur[j] += cur[j-data[i]]
print(cur[k])

