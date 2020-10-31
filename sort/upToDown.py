# 2분
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
for item in arr:
    print(item, end = ' ')