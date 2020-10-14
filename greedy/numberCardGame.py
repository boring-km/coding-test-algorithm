# 14분 21초
n, m = [int(i) for i in input().split()]
array = []
for i in range(n):
    array.append([int(j) for j in input().split()])

check = []
for i in range(n):
    check.append(min(array[i]))

print(max(check))