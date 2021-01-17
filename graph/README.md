# 이것이 코딩 테스트다 - 10장 그래프
- 1. 다양한 그래프 알고리즘
- 2. 팀 결성 (문제)
- 3. 도시 분할 계획 (문제)
- 4. 커리큘럼 (문제)
    
## 1. 다양한 그래프 알고리즘
- DFS/BFS, 최단 경로 역시 그래프 알고리즘임

### 1.1 서로소 집합
- 공통 원소가 없는 집합
- 트리를 사용해 구현
    - union 연산을 확인하여 서로 연결된 두 노드 A, B 확인
    1. A, B의 루트 노드를 각각 찾음
    2. A의 루트노드를 B의 루트노드의 부모노드로 설정한다.
    - 모든 union 연산 처리할 때까지 위의 과정 반복
    
```python

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    ## 해당 노드의 루트 노드가 바로 부모 노드가 되도록 수정
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])# return find_parent(parent, parent[x])
    return parent[x] # x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화하기

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력하기
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')
```

- 무방향 그래프에서 사이클이 발생했는지 판별할 수도 있음 [링크](https://github.com/boring-km/python-for-coding-test/blob/master/10/4.py)

### 1.2 신장 트리
- 하나의 그래프가 있을 때 **모든 노드**를 포함하면서 사이클이 존재하지 않는 부분 그래프
- 크루스칼 알고리즘(대표적인 최소 신장 트리 알고리즘)
    - 가장 적은 비용으로 모든 노드를 연결
    1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
    2. 간선을 하나씩 확인하며 현재 간선이 사이클을 발생시키는지 확인(발생하지 않을 때만 트리에 포함)
    3. 모든 간선에 대해 2번 반복
    
```python
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화하기

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력 받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
```

### 1.3 위상 정렬
- 순서가 정해져 있는 작업을 차례대로 수행해야 할 때
- 방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열하는 것'
    1. 진입차수가 0인 노드를 큐에 넣는다.
    2. 큐가 빌 때까지 반복
        - 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거
        - 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
    
```python
from collections import deque

# 노드의 개수와 간선의 개수를 입력 받기
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v + 1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 A에서 B로 이동 가능
    # 진입 차수를 1 증가
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')

topology_sort()
```

