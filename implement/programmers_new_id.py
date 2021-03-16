def solution(new_id):

    # level1
    level1 = new_id.lower()

    # level2
    level2 = ''
    for i in range(len(level1)):
        target = level1[i]
        target_ascii = ord(target)
        if 97 <= target_ascii <= 122 or target.isnumeric() or target == '-' or target == '_' or target == '.':
            level2 += level1[i]

    # level3
    level3 = ''
    for i in range(len(level2)):
        if i > 0 and level2[i] == '.' and level2[i-1] == '.':
            continue
        else:
            level3 += level2[i]

    # level4
    level4 = level3
    if level3[0] == '.':
        level4 = level3[1:]
    if level3[-1] == '.':
        level4 = level4[0:-1]

    # level5
    level5 = level4
    if len(level4) == 0:
        level5 = 'a'

    # level6
    level6 = level5
    if len(level5) >= 16:
        level6 = level5[0:15]
        if level6[-1] == '.':
            level6 = level6[0:-1]

    # level7
    level7 = level6
    if len(level6) <= 2:
        while len(level7) < 3:
            level7 += level6[-1]
    return level7


# solution("azbc")
# print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution("z-+.^."))
print(solution("abcdefghijklmn.p"))
