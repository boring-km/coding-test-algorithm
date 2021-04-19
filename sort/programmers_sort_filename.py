def solution(files):
    answer = []
    for file in files:
        number = -1
        number_end = -1
        for i in range(len(file)):
            if 48 <= ord(file[i]) <= 57:
                number = i
                break
        for i in range(number+1, len(file)):
            if ord(file[i]) < 48 or 57 < ord(file[i]):
                number_end = i
                break
        if number_end == -1:
            answer.append([file[0:number], file[number:]])
        else:
            answer.append([file[0:number], file[number:number_end], file[number_end:]])
    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))
    for i in range(len(answer)):
        if len(answer[i]) == 2:
            answer[i] = answer[i][0] + answer[i][1]
        else:
            answer[i] = answer[i][0] + answer[i][1] + answer[i][2]
    return answer


# ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))

