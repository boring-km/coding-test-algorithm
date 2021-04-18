from collections import deque


def solution(s):
    answer = 0
    size = len(s)
    is_a, is_b, is_c = 0, 0, 0
    q = deque(s)
    for i in range(size):
        check = True
        visited = ''
        for j in range(size):
            if q[j] == '[':
                is_a += 1
            elif q[j] == '{':
                is_b += 1
            elif q[j] == '(':
                is_c += 1
            elif q[j] == ']':
                if is_a <= 0 or visited == '(' or visited == '{':
                    check = False
                    break
                is_a -= 1
            elif q[j] == '}':
                if is_b <= 0 or visited == '(' or visited == '[':
                    check = False
                    break
                is_b -= 1
            elif q[j] == ')':
                if is_c <= 0 or visited == '[' or visited == '{':
                    check = False
                    break
                is_c -= 1
            visited = q[j]
        if check and is_a == 0 and is_b == 0 and is_c == 0:
            answer += 1
        q.append(q.popleft())

    return answer


print(solution("([]){}()"))
