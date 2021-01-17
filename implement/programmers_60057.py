# 전에 풀었던 문제

def solution(s):
    size, arr = len(s), []
    for i in range(1, size):    # 문자열 자르는 갯수마다 테스트
        text, temp, temp_s, num = s, "", "", 1
        for j in range(size+1):
            if temp == text[:i]:    # 현재 문자열와 같으면 이쪽
                num += 1
            elif j != 0 and temp != text[:i]:  # 2번째 문자열부터 앞 문자열과 다르다면
                if num == 1:    # 문자열이 한번이라면
                    temp_s += temp
                else:   # 문자열이 여러번 동일하게 온 것에 대해 앞에 숫자 붙이기
                    temp_s += str(num) + temp
                num = 1
            temp = text[:i]  # 첫번째이면 무조건 이쪽 먼저 들어감
            text = text[i:]
        arr.append(len(temp_s))  # 문자열 자르는 갯수마다 나온 갯수를 arr에 추가
    if size == 1:
        return 1
    else:
        return min(arr)