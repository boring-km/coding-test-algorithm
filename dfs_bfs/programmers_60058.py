"""
p는 짝수이고 균형잡힌 괄호 문자열임
"""


def dfs(p):
    if p == '':     # 1번 조건
        return p

    u, v = '', ''   # 2번 조건
    for i in range(2, len(p)+2, 2):
        item = p[:i]
        left, right = 0, 0
        for s in item:
            if s == '(':
                left += 1
            else:
                right += 1
        if left == right:
            u = item
            v = p[i:]
            break

    # 3번 조건
    must_be_plus = 0
    for s in u:
        if s == '(':
            must_be_plus += 1
        else:
            must_be_plus -= 1
        if must_be_plus < 0:    # 4번 조건
            break
    if must_be_plus == 0:    # 3번 조건 true -> v에 대해 1번부터 재귀
        return u + dfs(v)   # 3-1
    else:   # 4번 조건 수행
        temp = '('      # 4-1
        temp += dfs(v)  # 4-2
        temp += ')'     # 4-3
        # 4-4
        u = u[1:-1]
        u_temp = ''
        for item in u:
            if item == '(':
                u_temp += ')'
            else:
                u_temp += '('
        temp += u_temp
        return temp     # 4-5


def solution(p):
    answer = dfs(p)
    return answer


print(solution("(()())()"))
