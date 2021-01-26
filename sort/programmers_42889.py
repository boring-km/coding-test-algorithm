def solution(N, stages):
    answer = []
    data = [0] * (N + 1)
    temp_data = []
    for item in stages:
        for i in range(item):
            data[i] += 1
    print(data)
    for k in range(1, N + 1):
        if data[k - 1] == 0:
            temp_data.append([0, k])
        else:
            temp_data.append([1 - data[k] / data[k - 1], k])
    temp_data.sort(key=lambda x: (-x[0], x[1]))
    print("sorted:", temp_data)
    for item in temp_data:
        answer.append(item[1])

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))


