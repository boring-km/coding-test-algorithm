# https://velog.io/@tjdud0123/가사-검색-2020-카카오-공채-python
from collections import defaultdict
from bisect import bisect_left, bisect_right


def count_by_lange(temp_list, start, end):
    ## word에서 frozz가 들어갈 인덱스의 우측 인덱스
    ## word에서 froaa가 들어갈 인덱스의 좌측 인덱스    -> fro??가 있다면 이 두 인덱스 사이에 있는 것이다!!!!
    left = bisect_right(temp_list, end)
    right = bisect_left(temp_list, start)
    return left - right


def solution(words, queries):
    answer = []
    cands = defaultdict(list)
    reverse_cands = defaultdict(list)
    # 길이별 저장
    for word in words:
        cands[len(word)].append(word)
        reverse_cands[len(word)].append(word[::-1])
    # 정렬 O(NlogN)
    for cand in cands.values():
        cand.sort()
    for cand in reverse_cands.values():
        cand.sort()
    # 탐색 O(N * logM)
    for query in queries:
        if query[0] == '?': # 와일드카드 접두사 일 때
            temp_list = reverse_cands[len(query)]
            start, end = query[::-1].replace('?','a'), query[::-1].replace('?','z')
        else: # 와일드카드 접미사 일 때
            temp_list = cands[len(query)]
            start, end = query.replace('?','a'), query.replace('?','z')
        answer.append(count_by_lange(temp_list, start, end))

    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?", "?????"]))

