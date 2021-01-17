# 15분 정도
import heapq
import sys
input = sys.stdin.readline

n, m, c = map(int, input().split())

INF = int(1e9)
graph = [[] for i in range(n+1)]
time = [INF] * (n + 1)

for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))


# 개선된 다익스트라
def improved_dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0이고, 먼저 q에 삽입한다.
    heapq.heappush(q, (0, start))
    time[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if time[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < time[i[0]]:
                time[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


improved_dijkstra(c)
cityCount = 0
finalTime = 0
for i in range(1, m+1):
    if time[i] < INF:
        cityCount += 1
        finalTime = max(finalTime, time[i])

print(cityCount, finalTime)
