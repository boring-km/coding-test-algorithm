# 팰린드롬
# https://www.crocus.co.kr/1075


def solution(s):
    n = len(s)
    temp = "#"
    for i in range(n):
        temp += s[i]
        temp += '#'
    n = len(temp)
    a = [0 for _ in range(n)]

    # i보다 작은 모든 수 j에 대해 가장 큰 값을 내는 값을 p라고 하고, r = p + A[p]
    r, p = 0, 0
    for i in range(n):
        # i는 p를 중심으로 하는 팰린드롬 내부의 변수
        # i의 반대편 좌표는 p가 중심이므로 2p - i를 하면 반대편 좌표임
        if i <= r:
            a[i] = min(a[2*p - i], r-i)
        # i를 기준으로 a[i]+1 만큼 확인 (1은 사이마다 #을 넣었기 때문에
        while i - (a[i] + 1) >= 0 and i + (a[i] + 1) < n and \
                temp[i - (a[i] + 1)] == temp[i + (a[i] + 1)]:
            # print(i - (a[i] + 1),  + (a[i] + 1), temp[i - (a[i] + 1)])
            a[i] += 1
        if r < i + a[i]:
            r = i + a[i]
            p = i
    answer = max(a)
    print(temp)
    print(a)
    return answer


print(solution("abcdcba"))
