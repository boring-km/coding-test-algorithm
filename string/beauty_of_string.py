def solution(s):
    answer = 0
    size = len(s)
    check = dict()

    for i in range(size):
        if not check.get(s[i]):
            answer += i
        check[s[i]] = i

    return answer


print(solution("baby"))
