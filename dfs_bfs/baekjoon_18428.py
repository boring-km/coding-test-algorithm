n = int(input())
data = []
teacher_list = []
result = 0
visit = [[False] * n for _ in range(n)]
end = False

for i in range(n):
    temp = [_ for _ in input().split()]
    data.append(temp)
    for j in range(n):
        if temp[j] == 'T':
            teacher_list.append([i, j])

# 상하좌우
moveX = [-1, 1, 0, 0]
moveY = [0, 0, -1, 1]


def dfs(sty, stx, pre_y, pre_x, move, count):
    global end
    ty, tx = pre_y + moveY[move], pre_x + moveX[move]
    if ty < 0 or ty >= n or tx < 0 or tx >= n:
        return count
    if data[ty][tx] == 'T':
        return count
    elif data[ty][tx] == 'S':
        if data[pre_y][pre_x] == 'T':   # 불가능
            end = True
            return count
        if data[pre_y][pre_x] == 'X':
            if ty == sty:
                if tx < stx:
                    for t in range(pre_x, stx):
                        visit[ty][t] = True
                else:
                    for t in range(stx+1, pre_x):
                        visit[ty][t] = True
            if tx == stx:
                if ty < sty:
                    for t in range(pre_y, sty):
                        visit[t][tx] = True
                else:
                    for t in range(sty+1, pre_y):
                        visit[t][tx] = True
            return count + 1
    else:
        if visit[ty][tx]:
            return count
        return dfs(sty, stx, ty, tx, move, count)


for teacher in teacher_list:
    y, x = teacher[0], teacher[1]
    for i in range(4):
        result += dfs(y, x, y, x, i, 0)
        print(y, x, result)

# for i in range(n):
#     for j in range(n):
#         if visit[i][j]:
#             print(i, j)
print(result)
if result <= 3 and not end:
    print("YES")
if result > 3 or end:
    print("NO")

# 3
# X T T
# S X T
# S X T
