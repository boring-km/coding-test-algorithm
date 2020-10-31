# 7분
nk = [int(item) for item in input().split()]
n, k = nk[0], nk[1]

a = [int(_) for _ in input().split()]
b = [int(_) for _ in input().split()]

a.sort()
b.sort(reverse=True)

for i in range(k):

    if a[i] < b[i]:
        a[i] = b[i]

print(sum(a))