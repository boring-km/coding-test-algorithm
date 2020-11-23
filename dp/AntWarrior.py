# 37분 03초
n = int(input())
data = [int(i) for i in input().split()]
visited = [False] * n


def find(index, maxi):
    if index == n - 3:
        return maxi + data[index + 2]
    if index >= n - 2:
        return maxi

    if data[index + 2] >= data[index + 3]:
        visited[index + 2] = True
        return find(index + 2, maxi + data[index + 2])
    else:
        visited[index + 3] = True
        return find(index + 3, maxi + data[index + 3])


print(find(-2, 0))

