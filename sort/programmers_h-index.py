def solution(citations):
    answer = 0
    start, end = 1, max(citations)
    n = len(citations)
    while end - start >= 0:
        mid = (start + end) // 2
        pcount, mcount = 0, 0
        for i in range(n):
            if citations[i] >= mid:
                pcount += 1
                if pcount == mid:
                    break
            else:
                mcount += 1
                if mcount == mid:
                    break
        if pcount == mid:
            answer = max(answer, mid)
            start = mid + 1
        else:
            end = mid - 1
    return answer


print(solution([3, 0, 6, 1, 5]))