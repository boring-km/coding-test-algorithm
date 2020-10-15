# 9분 16초
n = input()
result = 0
for i in range(int(n) + 1):
    for j in range(60):
        for k in range(60):
            if str(i).find(n) != -1 or str(j).find(n) != -1 or str(k).find(n) != -1:
                result += 1

print(result)