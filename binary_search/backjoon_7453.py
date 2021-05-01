n = int(input())

a, b, c, d = [], [], [], []
for i in range(n):
    temp = [int(i) for i in input().split()]
    a.append(temp[0])
    b.append(temp[1])
    c.append(temp[2])
    d.append(temp[3])

left, right = dict(), dict()

for i in range(n):
    for j in range(n):
        if not left.get(a[i]+b[j]):
            left[a[i]+b[j]] = 1
        else:
            left[a[i]+b[j]] += 1
    for j in range(n):
        if not right.get(c[i]+d[j]):
            right[c[i]+d[j]] = 1
        else:
            right[c[i]+d[j]] += 1

right = sorted(right.items())


def binary_search(data, target):
    result = 0
    start, end = 0, len(data)-1
    while end - start >= 0:
        mid = int((start + end) / 2)
        if target + data[mid] == 0:
            result += 1
            break
        elif target + data[mid] < 0:
            start = mid + 1
        else:
            end = mid - 1
    return result


answer = 0
for item in left:
    answer += binary_search(right, item)

print(answer)

