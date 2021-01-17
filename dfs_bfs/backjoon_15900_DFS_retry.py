import sys
input = sys.stdin.readline

n = int(input())

result = 0
data = []
visited = [0] * (n+1)

for i in range(n+1):
    data.append([])

for i in range(n-1):
    item = [int(j) for j in input().split()]
    data[item[0]].append(item[1])
    data[item[1]].append(item[0])


def dfs(node, count):
    global result
    visited[node] = True
    for item in data[node]:
        if not visited[item]:
            dfs(item, count + 1)

    if node != 1 and len(data[node]) == 1:
        result += count + 1


dfs(1, 0)

if result % 2:
    print("Yes")
else:
    print("No")