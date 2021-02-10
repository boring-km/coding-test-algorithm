import sys
input = sys.stdin.readline
tc = int(input())


def bellman():
    # 벨만 포드
    answer = [1e9] * (n+1)
    result = "NO"
    for start in range(1, n+1):
        answer[start] = 0
        for a in range(1, n+1):
            for b in range(1, n+1):
                for item in road_list[b]:
                    if answer[b] == 1e9:
                        continue
                    if answer[item[0]] > answer[b] + item[1]:
                        answer[item[0]] = answer[b] + item[1]
        for a in range(1, n+1):
            for item in road_list[a]:
                if answer[a] == 1e9:
                    continue
                if answer[item[0]] > answer[a] + item[1]:
                    return "YES"
        answer = [1e9] * (n+1)
    return result


for i in range(tc):
    n, m, w = map(int, input().split())
    road_list = [[] for _ in range(n+1)]
    for j in range(m):
        s, e, t = map(int, input().split())
        road_list[s].append([e, t])
        road_list[e].append([s, t])
    for j in range(w):
        s, e, t = map(int, input().split())
        road_list[s].append([e, -t])

    print(bellman())
