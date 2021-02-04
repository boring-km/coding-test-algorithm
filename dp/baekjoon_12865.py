# https://reakwon.tistory.com/34

# TODO 배낭 알고리즘을 적용해야 한다.
from itertools import combinations

n, k = map(int, input().split())
dp = [0] * 100001
data = [[]]
for i in range(n):
    w, v = map(int, input().split())
    if w <= k:
        dp[w] = v
        data.append([w, v])
print(data)
comb_list = list(combinations([int(_) for _ in range(1, len(data))], 2))
visit = [0] * len(data)
for comb in comb_list:
    l, r = comb[0], comb[1]
    cur_weight = data[l][0] + data[r][0]
    cur_value = data[l][1] + data[r][1]
    if cur_weight <= k:
        if dp[cur_weight] < dp[data[l][0]] + dp[data[r][0]]:
            dp[cur_weight] = dp[data[l][0]] + dp[data[r][0]]

print(max(dp))
