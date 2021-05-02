def solution(gems):
    answer = []
    left, right = len(set(gems)), len(gems)
    find = left

    while right - left >= 0:
        mid = (left+right) // 2
        check = False
        temp = []
        for i in range(len(gems) - mid+1):
            t = set(gems[i:i+mid])
            target = len(t)
            if target == find:
                check = True
                temp = [i+1, i+mid]
                break
        if check:
            if not answer:
                answer = temp
            else:
                dist = answer[1] - answer[0]
                temp_dist = temp[1] - temp[0]
                if temp_dist < dist:
                    answer = temp[:]
                    right = mid - 1
                elif temp_dist == dist:
                    if temp[0] < answer[0]:
                        answer = temp[:]
                    right = mid - 1
                else:
                    left = mid + 1
        else:
            left = mid + 1

    return answer


print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
