# 시간 너무 오래 걸림
# https://codedrive.tistory.com/49
def solution(triangle):
    size = len(triangle)
    for i in range(1, size):
        for j in range(i+1):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                # 예외상황은 없다 (나중에 값이 더 큰것이 온다던지 하는) -> 이런 고민하다가 오히려 망친다.
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
    return max(triangle[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
