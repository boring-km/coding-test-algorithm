'''
# 조건
기둥(0): 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
보(1): 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
'''


# 기둥 조건
# 1 바닥 위에 있거나
# 2 보의 한쪽 끝 부분 위에 있거나,
# 3 다른 기둥 위에 있어야 함
def install_column(answer, param):
    x, y = param
    if y == 0:  # 1 바닥 위에 있는 기둥은 설치 가능
        answer.append([x, y, 0])
        return
    for ans in answer:
        a_x, a_y, a_a = ans
        if a_a == 1:    # 2 보
            # 같은 x좌표에 있는 보
            if a_x == x and a_y == y:
                check = True
                for dou_ans in answer:
                    b_x, b_y, b_b = dou_ans
                    if b_b == 1:
                        # 좌측에도 보가 있으면 False
                        if b_x == a_x - 1 and b_y == a_y:
                            check = False
                            break
                if check:
                    answer.append([x, y, 0])
                    return
            # 왼쪽에 있는 보
            if a_x == x - 1 and a_y == y:
                check = True
                for dou_ans in answer:
                    b_x, b_y, b_b = dou_ans
                    if b_b == 1:
                        # 우측에도 보가 있으면 False
                        if b_x == x and b_y == a_y:
                            check = False
                            break
                if check:
                    answer.append([x, y, 0])
                    return
        else:   # 3
            if a_x == x and a_y == y - 1:
                answer.append([x, y, 0])
                return


# 보 조건
# 1 한쪽 끝 부분이 기둥 위에 있거나
# 2 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 함
def install_bottom(answer, param):
    x, y = param
    for ans in answer:
        a_x, a_y, a_a = ans
        if a_a == 0:   # 1
            if a_x == x and a_y == y - 1:
                answer.append([x, y, 1])
                return
            if a_x == x + 1 and a_y == y - 1:
                answer.append([x, y, 1])
                return
        else:   # 2
            if a_x == x - 1 and a_y == y:
                for dou_ans in answer:
                    b_x, b_y, b_b = dou_ans
                    if b_b == 1:
                        if b_x == x + 1 and b_y == y:
                            answer.append([x, y, 1])
                            return


# 기둥
# 3 다른 기둥 위에 있어야 함
# 보
# 1 한쪽 끝 부분이 기둥 위에 있거나
def delete_column(answer, param):
    x, y = param
    index = -1
    for i in range(len(answer)):
        tx, ty, ta = answer[i]
        # pop 할 index
        if tx == x and ty == y and ta == 0:
            index = i
            break
    for item in answer:
        tx, ty, ta = item
        # 보 1
        if ta == 1 and ty == y + 1:
            if tx == x:
                for dou_item in answer:
                    dx, dy, da = dou_item
                    # 기둥 위의 두 보가 전부 있을 때 기둥을 뺄 수 있다.
                    if dx == x - 1 and dy == y + 1:
                        answer.pop(index)
                        return
                    # 다른 쪽 기둥에 의지하던 보면 기둥 뺄 수 있다.
                    if dx == x + 1 and dy == y and da == 0:
                        answer.pop(index)
                        return
                return  # 빠지면 안된다
            if tx == x - 1:
                for dou_item in answer:
                    dx, dy, da = dou_item
                    # 기둥 위의 두 보가 전부 있을 때 기둥을 뺄 수 있다.
                    if dx == x and dy == y + 1:
                        answer.pop(index)
                        return
                    # 다른 쪽 기둥에 의지하던 보면 기둥 뺄 수 있다.
                    if dx == x - 1 and dy == y and da == 0:
                        answer.pop(index)
                        return
                return  # 빠지면 안된다
    answer.pop(index)


# 기둥 조건
# 1 바닥 위에 있거나
# 2 보의 한쪽 끝 부분 위에 있거나,
# 3 다른 기둥 위에 있어야 함
# 보 조건
# 1 한쪽 끝 부분이 기둥 위에 있거나
# 2 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 함
def delete_bottom(answer, param):
    x, y = param
    index = -1
    for i in range(len(answer)):
        tx, ty, ta = answer[i]
        # pop 할 index
        if tx == x and ty == y and ta == 1:
            index = i
            break
    for item in answer:
        tx, ty, ta = item
        # 기둥이 한쪽만 의지하고 있으면 pass
        if ty == y and ta == 0:
            if tx == x:
                check = True
                for dou_item in answer:
                    dx, dy, da = dou_item
                    # 좌측 보에 의지하는 기둥도 아니면 기둥 절대 X
                    if dx == x - 1 and dy == y and da == 1:
                        check = False
                        return
                    # 밑에 기둥 있으면 삭제 가능
                    if dx == x and dy == y - 1 and da == 0:
                        answer.pop(index)
                        return
                if check:
                    return
            if tx == x + 1:
                check = True
                for dou_item in answer:
                    dx, dy, da = dou_item
                    # 우측 보에 의지하는 기둥도 아니면 기둥 절대 X
                    if dx == x + 1 and dy == y and da == 1:
                        check = False
                        return
                    # 밑에 기둥 있으면 삭제 가능
                    if dx == x and dy == y - 1 and da == 0:
                        answer.pop(index)
                        return
                if check:
                    return
        # 서로 연결된 보이면
        if ty == y and ta == 1:
            if tx == x - 1:
                check_count = 0
                for dou_item in answer:
                    dx, dy, da = dou_item
                    # 좌측 보가 버티는 경우
                    if dx == x - 1 and dy == y - 1 and da == 0:
                        check_count += 1
                    # 우측 보가 버티는 경우
                    if dx == x + 1 and dy == y - 1 and da == 0:
                        check_count += 1
                if check_count == 2:
                    answer.pop(index)
                    return
                else:
                    return
    answer.pop(index)


def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        if frame[3] == 1:   # 설치
            if frame[2] == 0:   # 기둥
                install_column(answer, frame[0:2])
            else:   # 보
                install_bottom(answer, frame[0:2])
        else:   # 삭제
            if frame[2] == 0:   # 기둥
                delete_column(answer, frame[0:2])
            else:   # 보
                delete_bottom(answer, frame[0:2])
    answer.sort()
    return answer


print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))