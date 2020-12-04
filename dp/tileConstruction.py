# 37분 59초
n = int(input())

result = [0, 1, 3, 5]

for i in range(4, n+1):
    if n % 2 == 0:
        result.append(result[i // 2] * result[i // 2])
    else:
        result.append(result[i // 2] * result[i // 2 + 1])
print(result[n])
