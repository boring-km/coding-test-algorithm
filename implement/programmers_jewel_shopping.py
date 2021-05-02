def solution(gems):
    final_size = len(set(gems))
    record = {gems[0]: 1}
    cur = [0, len(gems) - 1]
    start, end = 0, 0

    while start < len(gems) and end < len(gems):
        if len(record) == final_size:
            if end - start < cur[1] - cur[0]:
                cur = [start, end]
            if record[gems[start]] == 1:
                del record[gems[start]] # 딕셔너리 키 제거
            else:
                record[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if end == len(gems):
                break
            if gems[end] in record.keys():
                record[gems[end]] += 1
            else:
                record[gems[end]] = 1
    return [cur[0] + 1, cur[1] + 1]


print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
