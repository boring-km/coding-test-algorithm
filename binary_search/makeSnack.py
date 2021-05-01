# 50분 07초
n, m = [int(_) for _ in input().split()]
snackList = [int(_) for _ in input().split()]


def binary_search(data, limit):
    result = 0
    start, end = 0, data[-1]
    while end - start >= 0:
        mid = (start + end) // 2
        target = 0
        for item in data:
            if item >= mid:
                target += item - mid

        if target >= limit:
            start = mid + 1
            result = max(result, mid)
        else:
            end = mid - 1

    return result


print(binary_search(sorted(snackList), m))
