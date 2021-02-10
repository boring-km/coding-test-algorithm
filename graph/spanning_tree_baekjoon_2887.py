import sys
from itertools import permutations
from heapdict import heapdict

input = sys.stdin.readline
n = int(input())
permu = permutations([int(i) for i in range(n)], 2)
node_list = []
for i in range(n):
    x, y, z = map(int, input().split())
    node_list.append([x, y, z])

test = dict()
for item in permu:
    left, right = item[0], item[1]
    l, r = node_list[left], node_list[right]
    dist = min(abs(l[0]-r[0]), abs(l[1]-r[1]), abs(l[2]-r[2]))
    if test.get(left) is not None:
        test[left][right] = dist
    else:
        test[left] = dict()
        test[left] = {right: dist}


def prim(graph, start):
    mst, keys, pi, total = list(), heapdict(), dict(), 0
    for node in graph.keys():
        keys[node] = 1e12
        pi[node] = None
    keys[start], pi[start] = 0, start

    while keys:
        cur_node, cur_key = keys.popitem()
        mst.append([pi[cur_node], cur_node, cur_key])
        total += cur_key
        for adj, weight in test[cur_node].items():
            if adj in keys and weight < keys[adj]:
                keys[adj] = weight
                pi[adj] = cur_node
    return total


print(prim(test, 0))