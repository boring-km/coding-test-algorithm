# 포기함

n = int(input())
data = [[0, 0] for _ in range(n+10)]
dp = [0] * (n+1001)
for i in range(1, n+1):
    data[i] = [int(j) for j in input().split()]

answer = 0
for i in range(1, n+2):
    time, pay = data[i][0], data[i][1]
    answer = max(answer, dp[i])
    if time + i <= n + 1:    # 시간 초과하는건 갱신 X
        dp[time + i] = max(answer + pay, dp[time + i])
print(answer)
