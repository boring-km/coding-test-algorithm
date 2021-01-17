from itertools import combinations

n, m = map(int, input().split())
cities = []
houses = []
chickens = []
for y in range(n):
    cities.append([int(i) for i in input().split()])
    for x in range(n):
        if cities[y][x] == 2:
            chickens.append([y, x])
        elif cities[y][x] == 1:
            houses.append([y, x])

# 조합으로 경우의 수 전부 찾기 - 브루트포스
comb_check = []
for i in range(1, m+1): # index 전부 담기
    comb = list(combinations(chickens, i))
    comb_check.append(comb)

comb = []
for item in comb_check:
    for i in item:
        comb.append(i)

# 모든 경우의 수에서 나오는 index로 최단거리 찾기
result = 1e77
for data in comb:
    temp_sum = 0
    for h in range(len(houses)):
        temp = 1e77
        for chicken in data:
            dist = abs(chicken[0] - houses[h][0]) + abs(chicken[1] - houses[h][1])
            temp = min(temp, dist)
        temp_sum += temp
    result = min(result, temp_sum)

print(result)