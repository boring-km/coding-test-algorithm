def solution(number, k):
    answer = ''
    n = len(number)
    start, idx = 0, 0
    maxi = max(number)
    for i in range(n-k):
        find = number[start]    # 0이 아니라 이전 인덱스 다음의 값부터 생각함
        idx = start
        for j in range(start, i+k+1):   # 최대 n-1까지
            tar = number[j]
            if tar == maxi:
                find = tar
                idx = j
                break

            if find < tar:    # 최대 number 찾음
                find = tar
                idx = j
        start = idx + 1
        answer += find
    return answer


print(solution("4177252841", 4))
