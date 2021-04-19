def solution(m, musicinfos):
    answer = []
    m_arr = []
    for i in range(len(m)):
        if m[i] != '#':
            m_arr.append(m[i])
        else:
            m_arr[-1] += '#'
    size = len(m_arr)
    for item in musicinfos:
        array = item.split(",")
        sh, sm = map(int, array[0].split(":"))
        eh, em =  map(int, array[1].split(":"))
        name = array[2]
        music = []
        music_arr = array[3]
        for i in range(len(music_arr)):
            if music_arr[i] != '#':
                music.append(music_arr[i])
            else:
                music[-1] += '#'
        music_len = len(music)
        minutes = (eh-sh) * 60 + (em-sm)
        temp = []
        if music_len < minutes:
            count = minutes // music_len
            left = minutes % music_len
            for i in range(count):
                temp += music
            if left > 0:
                temp += music
        else:
            temp = music[0:minutes]
        for s in range(minutes-size+1):
            temp_cut = ""
            for st in temp[s:s+size]:
                temp_cut += st
            if temp_cut == m:
                answer.append([name, minutes])
    if len(answer) == 0:
        return '(None)'
    else:
        result = answer[0]
        for i in range(len(answer)):
            if result[1] < answer[i][1]:
                result = answer[i]
        for i in range(len(musicinfos)):
            temp = musicinfos[i].split(",")[2]
            if result[0] == temp:
                return temp
    return answer

print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
