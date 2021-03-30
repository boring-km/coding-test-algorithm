import math

def solution(w,h):
    answer = 1
    gcd = math.gcd(w, h)    # 최대 공약수
    area = w * h
    line = w + h - gcd
    return area - line