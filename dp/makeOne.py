# 20분 초과
# 교재 코드 보면서 연습
x = int(input())
memo = [0] * 30001

for i in range(2, x + 1):
    # 가장 느린 방법은 1씩 빼는 거니깐 반대로 생각
    memo[i] = memo[i-1] + 1
    # i 번째에 현재 방법으로 사용했을 때 더 작은 memo가 될 값으로 저장
    if i % 2 == 0:
        memo[i] = min(memo[i], memo[i//2] + 1)
    if i % 3 == 0:
        memo[i] = min(memo[i], memo[i//3] + 1)
    if i % 5 == 0:
        memo[i] = min(memo[i], memo[i//5] + 1)

print(memo[x])