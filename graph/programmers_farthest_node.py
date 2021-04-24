from collections import deque


def solution(n, edge):
    answer = 0
    visited = [-1 for _ in range(n+1)]
    # 2차원 배열
    graph = [[] for _ in range(n+1)]
    for e in edge:
        start, end = e[0], e[1]
        graph[start].append(end)
        graph[end].append(start)

    dist = 0
    q = deque([[1, dist]])
    while q:
        v, dist = q.popleft()
        if visited[v] == -1:
            visited[v] = dist
            dist += 1
            for e in graph[v]:
                q.append([e, dist])
    print(visited)
    for value in visited:
        if value == max(visited):
            answer += 1
    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
