# N개의 체커가 엄청 큰 보드 위에 있다. i번 체커는 (xi, yi)에 있다. 같은 칸에 여러 체커가 있을 수도 있다. 체커를 한 번 움직이는 것은 그 체커를 위, 왼쪽, 오른쪽, 아래 중의 한 방향으로 한 칸 움직이는 것이다.

# 입력
# 첫째 줄에 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 각 체커의 x좌표와 y좌표가 주어진다. 이 값은 1,000,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 수 N개를 출력한다. k번째 수는 적어도 k개의 체커가 같은 칸에 모이도록 체커를 이동해야 하는 최소 횟수이다.

n = int(input())

arr = []
x_list = []
y_list = []

answer = [int(1e9)] * n

for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
    x_list.append(a)
    y_list.append(b)

for y in y_list:
    for x in x_list:
        dist = []

        for tx, ty in arr:
            d = abs(tx-x) + abs(ty-y)
            dist.append(d)
        
        dist.sort()

        temp = 0
        for j in range(len(dist)):
            temp += dist[j]
            answer[j] = min(temp, answer[j])

print(*answer)

# # Python
# n = int(input())
# coordinates = [list(map(int, input().split())) for _ in range(n)]
# answer = [int(1e9)] * n # 모일 체커 수 별로 값을 저장할 배열

# for x in coordinates: # x 좌표 후보
#     for y in coordinates: # y 좌표 후보
#         costs = []
#         for ix, iy in coordinates: # 입력받은 좌표
#             # 현재 x,y 좌표와 입력받은 좌표의 거리를 비교한 값을 costs 배열에 입력
#             costs.append(abs(x[0] - ix) + abs(y[1] - iy))

#         # costs를 정렬하여
#         costs.sort()
#         cost = 0
#         for i in range(n):
#             # cost 에 순차적으로 더하면서
#             cost += costs[i]
#             # 해당 인덱스의 값(answer[i])와 현재 좌표의 거리(cost)와 비교하여 작은 값을 저장
#             answer[i] = min(answer[i], cost)

# print(*answer)