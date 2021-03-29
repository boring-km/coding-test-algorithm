from collections import deque


def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    cur = 0
    count = 0
    while len(people) > 0:
        if cur >= limit:
            answer += 1
            count = 0
            cur = 0
            continue
        if cur + people[-1] <= limit:
            if count == 0:
                count += 1
                cur += people.pop()
                if len(people) == 0:
                    answer += 1
            else:
                count = 0
                people.pop()
                cur = 0
                answer += 1
        else:
            if cur + people[0] <= limit:
                if count == 0:
                    count += 1
                    cur += people.popleft()
                    people[0] = 0
                else:
                    count = 0
                    people.popleft()
                    cur = 0
                    answer += 1
            else:
                answer += 1
                count = 1
                cur = people.pop()
                if len(people) == 0:
                    answer += 1

    return answer


print(solution([10], 100))
