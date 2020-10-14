# 11분 54초
n, k = [int(i) for i in input().split()]

result = 0

while True:
    if n == 1:
        print(result)
        break
    if n % k == 0:
        n = int(n/k)
    else:
        n -= 1
    result += 1