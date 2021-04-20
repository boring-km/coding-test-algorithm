from collections import deque


def solution(msg):
    answer = []
    cur = 26
    record = dict()
    for i in range(26):
        record[chr(i+65)] = i+1

    q = deque(list(msg))
    while q:
        cur += 1
        if len(q) == 1:
            answer.append(ord(q.popleft())-64)
            break
        if not record.get(q[0] + q[1]):
            temp = q[0]+q[1]
            record[temp] = cur
            answer.append(ord(q.popleft())-64)
        else:
            temp = q.popleft()
            check = False
            while q:
                if not record.get(temp + q[0]):
                    temp_q = temp
                    temp_q += q[0]
                    record[temp_q] = cur
                    answer.append(record[temp])
                    check = True
                    break
                else:
                    temp += q.popleft()
            if not check:
                answer.append(record[temp])
    return answer


print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
