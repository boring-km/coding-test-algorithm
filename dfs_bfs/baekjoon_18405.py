# 틀렸습니다.

import copy
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
graph = []
record = [[] for _ in range(k+1)]
for i in range(n):
    data = [int(i) for i in input().split()]
    graph.append(data)
    for j in range(n):
        if data[j] != 0:
            record[data[j]].append([i, j])  # 바이러스가 있는 위치만 저장한 리스트

s, x, y = map(int, input().split())
move_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visit = [[False] * n for _ in range(n)]
for _ in range(s):  # s초 동안 바이러스 전염
    for i in range(1, k+1):     # 바이러스 번호에 따라서 1번부터 k번 까지
        copy_record = copy.deepcopy(record[i])  # 전염시킬 준비가 된 리스트 (record[i])
        add_list = []
        for item in copy_record:    # 전염대상인 바이러스
            ty, tx = item
            if visit[ty][tx]:
                continue
            visit[ty][tx] = True
            for j in range(4):
                moved_y, moved_x = move_list[j][0] + ty, move_list[j][1] + tx
                if moved_y < 0 or moved_y >= n or moved_x < 0 or moved_x >= n:
                    continue
                if visit[moved_y][moved_x]:
                    continue
                visit[moved_y][moved_x] = True
                if graph[moved_y][moved_x] == 0:
                    graph[moved_y][moved_x] = i
                    add_list.append([moved_y, moved_x])
        record[i] = add_list

print(graph[x-1][y-1])
