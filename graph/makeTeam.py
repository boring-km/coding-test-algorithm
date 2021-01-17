# 팀 합치기? 두 학생을 합치기도 하고 비교도 하고 -> 서로소

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
n, m = map(int, input().split())
team = [0] * (n + 1)


# 특정 원소가 속한 집합을 찾기리
def find_team(team, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    ## 해당 노드의 루트 노드가 바로 부모 노드가 되도록 수정
    if team[x] != x:
        team[x] = find_team(team, team[x])
    return team[x]


# 두 원소가 속한 집합을 합치기
def include_team(team, a, b):
    a = find_team(team, a)
    b = find_team(team, b)
    if a < b:
        team[b] = a
    else:
        team[a] = b


# 팀 테이블상에서, 팀을 자기 자신으로 초기화
for i in range(1, n + 1):
    team[i] = i

# Union 연산을 각각 수행
for i in range(m):
    check, a, b = map(int, input().split())
    if check == 0:
        include_team(team, a, b)
    else:
        if find_team(team, a) != find_team(team, b):
            print("NO")
        else:
            print("YES")

# 팀 테이블 내용 출력하기
print('팀 테이블: ', end='')
for i in range(1, n + 1):
    print(team[i], end=' ')

