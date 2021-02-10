# https://reakwon.tistory.com/34

n, k = map(int, input().split())    # n: 물건의 갯수
data = []
dp = [[0] * (k+1) for _ in range(n)]
for i in range(n):
    w, v = map(int, input().split())
    if w <= k:
        data.append([w, v])
n = len(data)   # 준서가 들 수 있는 물건들의 갯수


# 배낭 알고리즘
def knapsack(cur, limit):
    if cur == n:    # 끝까지 가면
        return 0
    value = dp[cur][limit]
    # 현재 가치가 0일때만 진입
    if value != 0:
        return value
    # 배낭에 추가할 수 있는 무게라면 일단 추가해보고 그 value를 구한다.
    if data[cur][0] <= limit:
        value = knapsack(cur + 1, limit - data[cur][0]) + data[cur][1]
    # 새롭게 추가된 value가 있다면 다음 번을 먼저 탐색한 결과와 비교해서 큰 값으로 결정한다.
    # dp 갱신
    dp[cur][limit] = max(value, knapsack(cur + 1, limit))
    return dp[cur][limit]


print(knapsack(0, k))

