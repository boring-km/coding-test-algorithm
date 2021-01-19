n = int(input())
data = []
teacher_list = []
result = 0

for i in range(n):
    temp = [_ for _ in input().split()]
    data.append(temp)
    for j in range(n):
        if temp[j] == 'T':
            teacher_list.append([i, j])

# 상하좌우
moveX = [-1, 1, 0, 0]
moveY = [0, 0, -1, 1]


def dfs(pre_y, pre_x, move, count):
    ty, tx = pre_y + moveY[move], pre_x + moveX[move]
    if ty < 0 or ty >= n or tx < 0 or tx >= n:
        return count
    if data[ty][tx] == 'T':
        return count
    elif data[ty][tx] == 'S':
        if data[pre_y][pre_x] == 'T':
            return count
        else:
            return count + 1
    else:
        return dfs(ty, tx, move, count)


for teacher in teacher_list:
    y, x = teacher[0], teacher[1]
    for i in range(4):
        result += dfs(y, x, i, 0)

print(result)
print(data)
