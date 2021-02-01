# 풀이법을 몰라 포기함~
first = input()
second = input()


def lcs(f_str, s_str):
    answer = [0] * len(f_str)  # 첫번째 문자열 길이만큼 list 생성
    for i in range(len(f_str)):   # i, f_str[i]
        current = []
        for j in range(len(s_str)):   # j, s_str[j]
            if f_str[i] == s_str[j]:  # 철자가 똑같다면
                if i * j > 0:   # 0이 아니면
                    count = answer[j-1] + 1     # 이전 길이 + 1
                else:       # i나 j가 0이면
                    count = 1   # 처음이라면 0
            else:   # 철자가 다르다면 굳이 추가할 필요는 없지
                temp_count_first, temp_count_second = 0, 0
                if i > 0:   # 첫번째 문자열의 처음이 아니라면
                    temp_count_first = answer[j]  # 저장된 값
                if j > 0:   # 두번째 문자열의 처음이 아니라면
                    temp_count_second = current[-1]    # 가장 최근에 저장된 count
                count = max(temp_count_first, temp_count_second)
            current.append(count)   # 일치하는 문자 수(count) 저장
        answer = current    # answer 갱신
    print(answer)
    return answer[-1]   # 마지막까지 탐색하면?


print(lcs(first, second))

