def solution(user_id, banned_id):

    record = []
    users = dict()
    for user in user_id:
        users[user] = len(user)

    for ban in banned_id:
        size = len(ban)
        index_list = []
        check = []
        for s in range(size):
            if ban[s] != '*':
                index_list.append([s, ban[s]])

        for key in users.keys():
            target = users[key]
            count = 0
            if target == size:
                for index in index_list:
                    if key[index[0]] == index[1]:
                        count += 1
                if count == len(index_list):
                    check.append(key)

        record.append(check)

    def recursive(target_list, i, record_set, result_set):
        if i == len(target_list):
            result_set.add(''.join(sorted(record_set)))
        else:
            for item in target_list[i]:  # i번째 banned_id에 들어갈 후보들
                temp = set(record_set)
                temp.add(item)
                if len(temp) == len(record_set)+1:    # 추가됨
                    recursive(target_list, i + 1, temp, result_set)
        return result_set

    result = recursive(record, 0, set(), set())

    return len(result)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))

