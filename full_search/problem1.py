# https://www.acmicpc.net/problem/1816
c = int(input())

for i in range(c):
    a = int(input())

    for i in range(2, 1_000_001):
        if a % i == 0:
            print("NO")
            break
        if i == 1_000_000:
            print("YES")
