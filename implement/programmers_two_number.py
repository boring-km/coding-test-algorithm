from itertools import combinations


def solution(numbers):
    data = set()
    data_list = list(combinations(numbers, 2))
    for item in data_list:
        data.add(sum(item))
    data = list(data)
    data.sort()
    return data


print(solution([2,1,3,4,1]))