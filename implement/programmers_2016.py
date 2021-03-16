def solution(a, b):
    # 윤년 있음
    # a월 b일
    month_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week_list = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]

    count = sum(month_list[0:a-1]) + b
    point = count % 7
    answer = week_list[point]
    return answer


print(solution(5, 24))
# print(sum([31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]))
