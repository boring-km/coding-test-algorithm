# 2시간 25분 44초
n = int(input())
data = [[0 for _ in range(n+1)] for j in range(n+1)]
start = 0
check = -1
depth = 0
log = [0 for _ in range(n+1)]
leafList = [0 for _ in range(n + 1)]

for i in range(n-1):
    depthCount = [int(j) for j in input().split()]
    if i == 0:
        start = depthCount[0]
    data[depthCount[0]][depthCount[1]] = 1  # 부모 - 자식
    data[depthCount[1]][depthCount[0]] = 2  # 자식 - 부모?


def dfs(v, cost):
    global check, depth, leafList
    leafFlag = False

    size = len(data[v])
    if v == 1:
        check = cost
    for i in range(size):
        if data[v][i] != 0 and log[i] == 0:
            leafFlag = True
            log[i] = cost + 1
            depth = max(depth, log[i])
            dfs(i, log[i])
    if not leafFlag:
        leafList[v] = depth


log[start] = 1
dfs(start, 0)

d = 0


def getAnswer():
    odd, even = 0, 0
    for depthCount in leafList:
        if depthCount == 0:
            continue
        d = depthCount - check
        if d <= 1:
            return "Yes"
        if d % 2 == 0:
            even += 1
        else:
            odd += 1
    if odd == 0:
        return "No"
    elif odd % 2 == 1 and even % 2 == 0:
        return "Yes"
    else:
        return "No"


print(getAnswer())
