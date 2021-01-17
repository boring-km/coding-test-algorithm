# 13분 40초
n = int(input())
moveList = [c for c in input().split()]

traveler = [1, 1]

for i in range(len(moveList)):
    if moveList[i] == 'R' and traveler[0] < n:
        traveler[0] += 1
    elif moveList[i] == 'L' and traveler[0] > 1:
        traveler[0] -= 1
    elif moveList[i] == 'U' and traveler[1] > 1:
        traveler[1] -= 1
    elif moveList[i] == 'D' and traveler[1] < n:
        traveler[1] += 1
    else:
        continue

print(traveler[1], traveler[0])
