# 25분 정도
def solution(record):
    answer = []
    check = dict()
    id_record = []
    action_record = []
    for rec in record:
        temp = rec.split()
        if len(temp) == 3:
            action, uid, name = temp
            check[uid] = name
        else:
            action, uid = temp
        id_record.append(uid)
        action_record.append(action)

    for i in range(len(id_record)):
        name = check[id_record[i]]
        action = action_record[i]
        if action == "Enter":
            action = "들어왔습니다."
        elif action == "Leave":
            action = "나갔습니다."
        else:
            continue
        answer.append(name + "님이 " + action)
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
