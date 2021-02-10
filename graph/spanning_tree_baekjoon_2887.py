import sys
from itertools import permutations
from collections import defaultdict
from heapq import *

input = sys.stdin.readline
n = int(input())
permu = permutations([int(i) for i in range(n)], 2)
node_list = []
for i in range(n):
    x, y, z = map(int, input().split())
    node_list.append([x, y, z])

edges = []
for item in permu:
    left, right = item[0], item[1]
    l, r = node_list[left], node_list[right]
    dist = min(abs(l[0]-r[0]), abs(l[1]-r[1]), abs(l[2]-r[2]))
    edges.append([dist, str(left), str(right)])


def prim(first_node):
    mst = []
    adj_edges = defaultdict(list)
    for weight, node1, node2 in edges:
        adj_edges[node1].append([weight, node1, node2])
    connected = set(first_node)
    selected_edge = adj_edges[first_node]
    heapify(selected_edge)

    while selected_edge:
        weight, node1, node2 = heappop(selected_edge)
        if node2 not in connected:
            connected.add(node2)
            mst.append([weight, node1, node2])
            for edge in adj_edges[node2]:
                if edge[2] not in connected:
                    heappush(selected_edge, edge)
    answer = 0
    for temp_node in mst:
        answer += temp_node[0]
    return answer


print(prim('0'))

