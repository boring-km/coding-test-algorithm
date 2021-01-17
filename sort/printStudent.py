n = int(input())
arr = []
for i in range(n):
    data = input().split()
    arr.append([int(data[1]), data[0]])

arr.sort()

for item in arr:
    print(item[1], end=' ')