# https://www.acmicpc.net/problem/2503
# A가 정답으로 생각할 수 있는 모든 수를 넣어보기
# B가 도전한 내용에 맞는지

n = int(input())

answer = 0

hint = [list(map(int, input().split())) for _ in range(n)]

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if a == b or b == c or c == a:
                continue
            cnt = 0
            for arr in hint:
                number = arr[0]
                strike = arr[1]
                ball = arr[2]
                # a, b, c 라는 숫자를 number하고 비교해서
                # 자리수를 나눠서 strike ball을 측정하는 부분
                ball_count = 0
                strike_count = 0

                d, e, f = number // 100, number % 100 // 10, number % 10

                if a == d:
                    strike_count += 1
                if a == e or a == f:
                    ball_count += 1

                if b == e:
                    strike_count += 1
                if b == d or b == f:
                    ball_count += 1

                if c == f:
                    strike_count += 1
                if c == d or c == e:
                    ball_count += 1

                if ball == ball_count and strike == strike_count:
                    cnt += 1
            if cnt == n:
                answer += 1

print(answer)
