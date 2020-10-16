# 1시간 시도했지만 결과 못 구함
# TODO: 풀이보고 다시 공부해보기
n, m = [int(i) for i in input().split()]
a, b, d = [int(i) for i in input().split()]
data = [[int(i) for i in input().split()] for _ in range(n)]
visited = [[False] * m] * n

# 북동남서
moveX = [0, 1, 0, -1] * 2
moveY = [-1, 0, 1, 0] * 2

visited[b][a] = True
result = 1
flag = True

while flag:
    for i in range(d+1, d+4):
        x = a + moveX[i]
        y = b + moveY[i]
        if data[y][x] == 0 and visited[y][x] is False:
            if d < 3:
                d += 1
            else:
                d = 0
            result += 1
            visited[y][x] = True
            a = x
            b = y
            break

        if i == d+3:
            if d < 3:
                d += 1
            else:
                d = 0
    print(x, y, a, b, result)

print(result)