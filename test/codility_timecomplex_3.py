def solution(A):
    # 이분 탐색??
    total_sum = sum(A)
    start, end = 0, len(A)-1
    mid = (start+end) // 2
    answer = 1e9

    while end - start > 0:
        mid = (start+end) // 2

        first = sum(A[0:mid])
        second = total_sum - first
        check = second - first
        answer = min(answer, abs(check))

        if check == 0:
            break
        elif check < 0:
            end = mid - 1
        else:
            start = mid + 1

    first_front = sum(A[0:mid-1])
    second_front = total_sum-first_front
    check_front = abs(second_front - first_front)

    first_back = sum(A[0:mid+1])
    second_back = total_sum-first_back
    check_back = abs(second_back - first_back)

    answer = min(answer, check_front, check_back)
    return answer


print(solution([3, 1, 2, 4, 3]))