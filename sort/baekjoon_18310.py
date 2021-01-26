# 그냥 가운데에 있는거..?
n = int(input())
data = sorted([int(i) for i in input().split()])
print(data[(n-1) // 2])