from collections import deque


def solution(n, edge):
    answer = 0

    record = dict()
    graph = dict()
    for e in edge:
        start, end = e
        if graph.get(start):
            graph[start].append(end)
        else:
            graph[start] = [end]
        if graph.get(end):
            graph[end].append(start)
        else:
            graph[end] = [start]

    start = [[1, 0]]  # 노드 번호와, 현재 이동 거리
    visited = [1]
    q = deque(start)
    while q:
        node, dist = q.popleft()
        if graph.get(node):
            for next_node in graph.get(node):
                if next_node and next_node not in visited:
                    q.append([next_node, dist+1])
                    visited.append(next_node)
                    record[next_node] = dist+1

    maxi = max(record.values())
    for key in record.keys():
        if record[key] == maxi:
            answer += 1

    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
