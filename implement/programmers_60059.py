import copy


g_visit = set()


def rotate(key, count):
    m = len(key)
    result = [[0] * m for _ in range(m)]
    for i in range(count):
        for y in range(m):
            for x in range(m):
                result[x][(m-1)-y] = key[y][x]
        key = result
        result = [[0] * m for _ in range(m)]
    return key


def check_answer(key, lock):
    n = len(lock)
    m = len(key)

    for y_move in range(n - m + 1):
        for x_move in range(n - m + 1):
            copy_lock = copy.deepcopy(lock)
            for y in range(m):
                for x in range(m):
                    copy_lock[y+y_move][x+x_move] += key[y][x]
            count = 0
            for y in range(n):
                for x in range(n):
                    if copy_lock[y][x] == 1:
                        count += 1
            if count == n * n:
                return True

    return False


def left_move(key, count):
    m = len(key)

    for i in range(count):
        for y in range(m):
            for x in range(1, m + 1):
                if x == m:
                    key[y][x-1] = 0
                else:
                    key[y][x-1] = key[y][x]
    return key


def right_move(key, count):
    m = len(key)
    for i in range(count):
        for y in range(m):
            for x in range(m-1, -1, -1):
                if x == 0:
                    key[y][x] = 0
                else:
                    key[y][x] = key[y][x-1]
    return key


def down_move(key, count):
    m = len(key)
    for i in range(count):
        for y in range(m-1, -1, -1):
            if y == 0:
                key[y] = [0] * m
            else:
                key[y] = key[y-1]
    return key


def up_move(key, count):
    m = len(key)
    for i in range(count):
        for y in range(m):
            if y == m-1:
                key[y] = [0] * m
            else:
                key[y] = key[y+1]
    return key


def left_up(i, j, key, lock):
    temp = left_move(key, i)
    temp = up_move(temp, j)
    result = check_answer(temp, lock)
    return result


def right_down(i, j, key, lock):
    temp = right_move(key, i)
    temp = down_move(temp, j)
    result = check_answer(temp, lock)
    return result


def right_up(i, j, key, lock):
    temp = right_move(key, i)
    temp = up_move(temp, j)
    result = check_answer(temp, lock)
    return result


def left_down(i, j, key, lock):
    temp = left_move(key, i)
    temp = down_move(temp, j)
    result = check_answer(temp, lock)
    return result


def solution(key, lock):
    m = len(key)

    for i in range(m):  # key x 움직이는 거리
        for j in range(m):  # key y
            visit = set()
            for k in range(4):  # 회전
                temp = rotate(copy.deepcopy(key), k)
                pre_size = len(visit)
                visit.add(str(temp))
                post_size = len(visit)
                if pre_size == post_size:
                    continue
                if left_down(i, j, copy.deepcopy(temp), lock):
                    return True
                elif left_up(i, j, copy.deepcopy(temp), lock):
                    return True
                elif right_down(i, j, copy.deepcopy(temp), lock):
                    return True
                elif right_up(i, j, copy.deepcopy(temp), lock):
                    return True
                else:
                    continue
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
