def solution(stones, k):

    answer = min(stones)
    left, right = min(stones), max(stones)

    while right - left >= 0:
        mid = (left + right) // 2
        count = 0
        find = -1
        for i in range(len(stones)):
            if stones[i] <= mid:
                count += 1
            else:
                count = 0
            if count >= k:
                find = max(find, count)

        if find >= k:
            right = mid - 1
        else:
            answer = max(mid+1, answer)
            left = mid + 1

    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
