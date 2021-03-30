def solution(number, k):
    answer = ''
    n = len(number)
    idx = 0
    check = 0

    for i in range(n-k):
        find = 0
        for j in range(idx+1, n + 1 - (k - check)):
            left, right = check + n - j, n - k
            if left < right:
                break

            if find < int(number[j]):
                find = int(number[j])
                idx = j
        check += 1
        answer += number[idx]
    return answer




print(solution("1924", 2))
