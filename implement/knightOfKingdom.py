# 10분 16초
target = input()
x, y = ord(target[0])-97, int(target[1])

moveX = [1, 2, 2, 1, -1, -2, -2, -1]
moveY = [-2, -1, 1, 2, 2, 1, -1, -2]

result = 0
for i in range(len(moveX)):
    distX = x + moveX[i]
    distY = y + moveY[i]

    if 0 <= distX < 8 and 1 <= distY <= 8:
        result += 1

print(result)