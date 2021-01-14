# 20분 정도
data = input()
cur = data[0]
c1 = 0
c2 = 0

for i in range(1, len(data)):
    if data[i] != cur:
        if cur == '0':
            c1 += 1
        else:
            c2 += 1
    cur = data[i]

if data[-1] == '0':
    c1 += 1
else:
    c2 += 1
print(min(c1, c2))

# 000110011
