# https://reakwon.tistory.com/34

n, k = map(int, input().split())
data = []
dp = [[0] * (k+1) for _ in range(n)]
for i in range(n):
    w, v = map(int, input().split())
    if w <= k:
        data.append([w, v])
n = len(data)


# 배낭 알고리즘
def knapsack(cur, limit):
    if cur == n:    # 끝까지 가면
        return 0
    weight = dp[cur][limit]
    if weight != 0:
        return weight
    if data[cur][0] <= limit:
        weight = knapsack(cur + 1, limit - data[cur][0]) + data[cur][1]
    weight = max(weight, knapsack(cur + 1, limit))
    dp[cur][limit] = weight
    return dp[cur][limit]


print(knapsack(0, k))

