def solution(n, lost, reserve):
    answer = 0
    student = [1] * n
    for idx in reserve:
        student[idx-1] += 1
    for idx in lost:
        student[idx-1] -= 1
    for i in range(n):
        if student[i] == 2:
            if i == 0:
                if student[i+1] == 0:
                    student[i] -= 1
                    student[i+1] += 1
            elif 0 < i < n-1:
                if student[i-1] == 0:
                    student[i] -= 1
                    student[i-1] += 1
                elif student[i+1] == 0:
                    student[i] -= 1
                    student[i+1] += 1
            else:
                if student[i-1] == 0:
                    student[i] -= 1
                    student[i-1] += 1
    for item in student:
        if item > 0:
            answer += 1
    return answer


print(solution(5, [2, 4], [1, 3, 5]))
