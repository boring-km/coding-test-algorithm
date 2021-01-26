import sys
input = sys.stdin.readline

# TODO 힙 사용하는 방식으로 바꿔보기
n = int(input())
data = []
for i in range(n):
    data.append(int(input()))
data.sort()


def dfs(card, extra):
    while len(card) > 1:
        card.sort()
        extra += card[0] + card[1]
        del card[0]
        del card[0]
        card.append(extra)
    return sum(card)


if n == 1:
    print(data[0])
elif n == 2:
    print(data[0] + data[1])
else:
    print(dfs(data, 0))

# 5
# 10 10 20 20 50