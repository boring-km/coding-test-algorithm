# https://dev-note-97.tistory.com/235
import sys

sys.setrecursionlimit(2500)


def solution(k, room_number):
    n = len(room_number)
    answer = [0 for _ in range(n)]
    record = dict()

    # Union Find 알고리즘
    def find_empty_room(num):
        if not record.get(num):
            record[num] = num + 1
            return num
        next_room = record[num]
        found_room = find_empty_room(next_room)
        record[num] = found_room
        return found_room

    for i in range(n):
        answer[i] = find_empty_room(room_number[i])

    return answer


print(solution(10, [1, 3, 4, 1, 3, 1]))
