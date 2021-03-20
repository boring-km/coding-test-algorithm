# 전에 자바로 풀이하다가 틀린 문제
# https://wwlee94.github.io/category/algorithm/bfs-dfs/travel-route/
from collections import defaultdict


def solution(tickets):
    # 특정 티켓의 인접 리스트를 구하는 함수
    def init_graph():
        routes = defaultdict(list)
        for key, value in tickets:
            routes[key].append(value)
        return routes

    # 재귀 호출을 사용한 DFS
    def dfs(key, footprint):
        if len(footprint) == N + 1:
            return footprint

        for idx, country in enumerate(routes[key]):
            routes[key].pop(idx)

            fp = footprint[:]  # deepcopy
            fp.append(country)

            retry = dfs(country, fp)
            if retry:
                return retry  # 모든 티켓을 사용해 통과한 경우

            routes[key].insert(idx, country)  # 통과 못했으면 티켓 반환

    routes = init_graph()
    for r in routes:
        routes[r].sort()

    N = len(tickets)
    answer = dfs("ICN", ["ICN"])  # 시작 경로

    return answer


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
