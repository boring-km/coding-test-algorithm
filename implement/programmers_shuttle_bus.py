def solution(n, t, m, timetable):
    size = len(timetable)
    time_list = [0 for _ in range(size + 1)]
    timetable.sort()
    for i in range(size):
        hh = int(timetable[i][0:2])
        mm = int(timetable[i][3:5])
        time_list[i] = hh * 60 + mm

    result = 0
    bus_time = 540
    index = 0

    for i in range(n):
        count = 0
        for j in range(index, size):
            if time_list[index] <= bus_time:
                index += 1
                count += 1
            if count == m:
                break
        if i == n - 1:  # 마지막까지 탐색 중이라면
            if count == m:   # timetable도 모두 탐색했다면
                result = time_list[index - 1] - 1
            else:
                result = bus_time
        bus_time += t   # t분 간격
        if bus_time >= 24 * 60:
            break

    res_hour = result // 60
    hour = "0" + str(res_hour) if res_hour < 10 else str(res_hour)
    res_min = result % 60
    minute = "0" + str(res_min) if res_min < 10 else str(res_min)

    return hour + ":" + minute


print(solution(10, 60, 45,
               ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
                "23:59", "23:59", "23:59", "23:59", "23:59"]))
