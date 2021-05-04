def solution(k, room_number):
    answer = []
    record = dict()
    for num in room_number:
        if not record.get(num):
            record[num] = True
            answer.append(num)
        else:
            temp = num + 1
            while True:
                if not record.get(temp):
                    record[temp] = True
                    answer.append(temp)
                    break
                temp += 1

    return answer
