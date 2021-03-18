def solution(priorities, location):
    answer = 0
    n = len(priorities)
    data = []
    maxi = max(priorities)
    for i in range(n):
        data.append([i, priorities[i]])

    priorities.sort()

    while True:
        target = data.pop(0)
        if target[1] == maxi:
            answer += 1
            if target[0] == location:
                return answer
            priorities.pop()
            maxi = priorities[-1]
        else:
            data.append(target)


print(solution([2, 1, 3, 2], 2))
# A B C D
# --
# B C D A
# C D A B (3 2 2 1)