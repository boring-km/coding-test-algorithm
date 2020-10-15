# 11분 54초
n, k = [int(i) for i in input().split()]

result = 0

while n != 1:
    if n % k == 0:
        n = int(n/k)
    else:
        n -= 1
    result += 1

print(result)
