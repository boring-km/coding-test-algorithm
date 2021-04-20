# 40분 정도 걸림
def solution(n, t, m, p):
    answer = ''
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    # n 진법, t번 대답함, 게임 인원 m, 나의 순서 p
    record = ""
    count = 0
    cur = p-1
    while len(answer) < t:
        if n > count:
            record += numbers[count]
        else:
            record += numeral(n, count)
        if len(record) > cur:
            answer += record[cur]
            cur += m
        count += 1
    return answer


def numeral(n, num):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    count = num // n
    left = num % n
    if count >= n:
        return numeral(n, count) + numbers[left]

    return numbers[count] + numbers[left]


# print(numeral(2, 10))

# 1101
# 111111
print(solution(16, 16, 2, 1))
