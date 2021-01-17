# 14분 21초
n, m = [int(i) for i in input().split()]
array = [[int(j) for j in input().split()] for _ in range(n)]
check = [min(array[i]) for i in range(n)]
print(max(check))
