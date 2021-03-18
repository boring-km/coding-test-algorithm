def solution(genres, plays):
    answer = []
    n = len(genres)
    genre_dict = dict()
    check_dict = dict()
    for i in range(n):
        genre = genre_dict.get(genres[i])
        if genre is not None:
            genre_dict[genres[i]] = genre + plays[i]
            check_list = check_dict[genres[i]]
            check_list.append([plays[i], i])
            check_dict[genres[i]] = check_list
        else:
            genre_dict[genres[i]] = plays[i]
            check_dict.setdefault(genres[i], [[plays[i], i]])

    genre_rank = []
    for genre in genre_dict.keys():
        genre_rank.append([genre_dict[genre], genre])

    genre_rank.sort(reverse=True)
    for genre in genre_rank:
        target = check_dict.get(genre[1])
        high_list = sorted(target, key=lambda x: (-x[0], x[1]))
        if len(high_list) == 1:
            answer.append(high_list[0][1])
        else:
            for i in range(2):
                answer.append(high_list[i][1])

    return answer


# print(solution(["classic", "pop", "classic", "classic", "pop"], [600, 500, 150, 600, 2500]))

print(solution(["classic"], [200]))
