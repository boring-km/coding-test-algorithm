from collections import deque


def find_only_one_diff(a, b):
    n = len(a)
    c = 0
    for i in range(n):
        if a[i] != b[i]:
            c += 1
    if c == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    answer = 0
    n = len(words)
    data_queue = deque([[0, begin]])
    visited = dict()
    while data_queue:
        temp = data_queue.popleft()

        if temp[1] == target:
            answer = temp[0]
            break
        for i in range(n):
            if find_only_one_diff(temp[1], words[i]) and visited.get(words[i]) is None:
                data_queue.append([temp[0]+1, words[i]])
                visited[words[i]] = temp[0]+1

    return answer



arr = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution("hit", "cog", arr))
