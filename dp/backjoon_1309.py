n = int(input())

a, b, res = 3, 7, 0
if n == 1:
    res = a
elif n == 2:
    res = b
else:
    for i in range(3, n+1):
        res = b * 2 + a
        a = b
        b = res

print(res % 9901)