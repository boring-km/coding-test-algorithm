from itertools import combinations

# 풀이시간: 1시간 40분
def solution(relation):
    col = len(relation[0])  # 1 ~ 8
    row = len(relation)

    unique_keys = []
    comb_array = range(col)
    for i in range(1, col+1):
        comb = list(combinations(comb_array, i))
        temp = []
        for item in comb:
            final_count = 0
            for key in unique_keys:
                count = 0
                for s in item:
                    if s in key:
                        count += 1
                if count != len(key):
                    final_count += 1
                else:
                    break
            if final_count == len(unique_keys):
                temp.append(item)

        if len(unique_keys) == 0:
            temp = comb
        for item in temp:   # item은 tuple
            keys = dict()
            is_unique = True
            for j in range(row):
                target = ""
                for s in item:
                    target += relation[j][s] + ","
                if not keys.get(target):
                    keys[target] = True
                else:
                    is_unique = False
                    break
            if is_unique:
                unique_keys.append(item)
    answer = len(unique_keys)
    return answer


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
