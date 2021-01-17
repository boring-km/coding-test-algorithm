# 10분 정도
INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    city1, city2 = map(int, input().split())
    graph[city1][city2] = 1
    graph[city2][city1] = 1

for city1 in range(1, n+1):
    for city2 in range(1, n+1):
        if city1 == city2:
            graph[city1][city1] = 0

X, K = map(int, input().split())

for stopover in range(1, n + 1):
    for city1 in range(1, n + 1):
        for city2 in range(1, n + 1):
            # 경유할 때 더 빨라질 수도 있지
            graph[city1][city2] = min(graph[city1][city2], graph[city1][stopover] + graph[stopover][city2])

result = graph[1][K] + graph[K][X]
if result >= INF:
    print(-1)
else:
    print(result)
