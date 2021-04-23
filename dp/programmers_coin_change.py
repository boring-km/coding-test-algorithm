def solution(n, money):
    size = len(money)
    dp = [0 for _ in range(n+1)]
    for i in range(n+1):    # 초기값 설정
        if i % money[0] == 0:
            dp[i] = 1
        else:
            dp[i] = 0
    print("---")
    print(dp)
    print("---")
    for i in range(1, size):
        for j in range(money[i], n+1):
            dp[j] += dp[j-money[i]]  # 각 숫자들을 더한 기록을 계속해서 갱신
            print(i, j, dp)

    answer = int(dp[n] % 1000000007)    # n 위치에 정확히 도달한 값들을 구함

    return answer


print(solution(10, [2, 3, 5]))

