def solution(words, queries):
    answer = []
    front = dict()
    back = dict()

    for word in words:
        f = word[0]
        b = word[-1]

        if not front.get(f):
            front[f] = dict()
            front[f][word] = len(word)
        else:
            front[f][word] = len(word)
        if not back.get(b):
            back[b] = dict()
            back[b][word] = len(word)
        else:
            back[b][word] = len(word)

    print(front)

    for q in queries:
        count = 0
        if q[0] != '?':
            index = len(q)-1
            for i in range(len(q)):
                if q[i] == '?':
                    index = i-1
                    break
            if front.get(q[0]):
                for key in front[q[0]].keys():
                    if key[0:index+1] == q[0:index+1] and front[q[0]][key] == len(q):
                        count += 1
        else:
            index = 0
            for i in range(len(q)):
                if q[i] != '?':
                    index = i
                    break
            if back.get(q[-1]):
                for key in back[q[-1]].keys():
                    if key[index:] == q[index:] and back[q[-1]][key] == len(q):
                        count += 1
        answer.append(count)

    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))