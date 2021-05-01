# 16분 52초
n = int(input())
partList = [int(_) for _ in input().split()]
partList.sort()
m = int(input())
targetList = [int(_) for _ in input().split()]


def binary_search(data, target):
    start, end = 0, len(data)-1
    while end - start >= 0:
        mid = (start + end) // 2
        if data[mid] == target:
            return "yes"
        elif data[mid] > target:
            end = mid - 1
        elif data[mid] < target:
            start = mid + 1
    return "no"


for i in range(m):
    temp = targetList[i]
    result = binary_search(partList, temp)
    print(result, end=' ')
