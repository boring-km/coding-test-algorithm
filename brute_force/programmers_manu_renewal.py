# 참고: https://dev-note-97.tistory.com/128
from itertools import combinations


def solution(orders, course):
    answer = []
    for cs in course:
        temp = []
        for order in orders:
            comb = combinations(sorted(order), cs)
            temp += comb

        counter_dict = dict()
        for item in temp:
            if counter_dict.get(item) is None:
                counter_dict[item] = 1
            else:
                counter_dict[item] += 1

        if len(counter_dict.keys()) > 0 and max(counter_dict.values()) != 1:
            for key in counter_dict.keys():
                if counter_dict[key] == max(counter_dict.values()):
                    answer += [''.join(key)]

    return sorted(answer)


result = solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])
print(result)
