import heapq
import sys
input = sys.stdin.readline

n, e = map(int, input().split())
data = [[] for _ in range(n+1)]
distance = [1e9] * (n+1)

for i in range(e):
    a, b, c = map(int, input().split())
    data[a].append([b, c])
    data[b].append([a, c])

v1, v2 = map(int, input().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0
    while q:
        dist, now = map(int, heapq.heappop(q))
        if distance[now] < dist:    # distance에 1e9 들어가 있었는데 갱신되면 이 조건에 들어감
            continue
        for item in data[now]:
            connected_dist = dist + item[1]
            if connected_dist < distance[item[0]]:  # 현재 now 위치에서 연결된 점과의 거리 (저장 안되어있으면 1e9)
                distance[item[0]] = connected_dist
                heapq.heappush(q, [connected_dist, item[0]])


dijkstra(1)
v1_first = distance[v1]
v2_first = distance[v2]
distance = [1e9] * (n+1)

dijkstra(v1)
v1_second = distance[v2]
distance = [1e9] * (n+1)
dijkstra(v2)
v1_last = distance[n]
distance = [1e9] * (n+1)
check1 = v1_first + v1_second + v1_last

dijkstra(v2)
v2_second = distance[v1]
distance = [1e9] * (n+1)
dijkstra(v1)
v2_last = distance[n]
check2 = v2_first + v2_second + v2_last

answer = min(check1, check2)

if answer >= 1e9:
    print(-1)
else:
    print(answer)

