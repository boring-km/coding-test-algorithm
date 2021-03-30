from collections import deque


def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    cur = 0
    count = 0
    while len(people) > 0:
        if cur >= limit:
            answer, count, cur = plus_another_boat(answer)
            continue
        count += 1
        if cur + people[-1] <= limit:
            if count == 1:
                cur += people.pop()
                if len(people) == 0:
                    answer += 1
            else:
                people.pop()
                answer, count, cur = plus_another_boat(answer)
        else:
            if cur + people[0] <= limit:
                if count == 1:
                    cur += people.popleft()
                    people[0] = 0
                else:
                    people.popleft()
                    answer, count, cur = plus_another_boat(answer)
            else:
                answer += 1
                count = 1
                cur = people.pop()
                if len(people) == 0:
                    answer += 1

    return answer


def plus_another_boat(answer):
    answer += 1
    count = 0
    cur = 0
    return answer, count, cur


print(solution([10], 100))
