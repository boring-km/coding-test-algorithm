from itertools import combinations


def solution(nums):
    answer = 0
    n = len(nums)

    all_case = list(combinations(nums, 3))
    for case in all_case:
        tar = sum(case)
        check = True
        i = 1
        for i in range(2, tar - 1, i*i):
            if tar % i == 0:
                check = False
                break
        if check:
            answer += 1

    return answer


print(solution([1, 2, 7, 6, 4]))
