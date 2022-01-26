def solution(rows, columns, queries):
    answer = []
    graph = []
    for i in range(rows):
        graph.append([i * columns + j + 1 for j in range(columns)])
    print(graph)

    def rotate(query):
        sy, sx, ey, ex = query
        sy, sx, ey, ex = sy - 1, sx - 1, ey - 1, ex - 1
        mini = rows * columns
        record = []
        for y in range(sy, ey+1):
            for x in range(sx, ex+1):
                if y == sy and x == sx:
                    record.append([y, x+1, graph[y][x]])
                elif y == sy and x != sx and x != ex:
                    record.append([y, x+1, graph[y][x]])
                elif y == sy and x == ex:
                    record.append([y+1, x, graph[y][x]])
                elif y != sy and y != ey and x == ex:
                    record.append([y+1, x, graph[y][x]])
                elif y == ey and x == ex:
                    record.append([y, x-1, graph[y][x]])
                elif y == ey and x != sx and x != ex:
                    record.append([y, x-1, graph[y][x]])
                elif y == ey and x == sx:
                    record.append([y-1, x, graph[y][x]])
                elif y != ey and y != sx and x == sx:
                    record.append([y-1, x, graph[y][x]])
                else:
                    continue
        for rec in record:
            y, x, value = rec
            mini = min(mini, value)
            graph[y][x] = value

        return mini

    for q in queries:
        mini = rotate(q)
        answer.append(mini)

    return answer


# 1 2 3 4
# 5 6 7 8

# print(solution(6, 6, [[2, 2, 5, 4], [2, 2, 5, 4], [2, 2, 5, 4], [2, 2, 5, 4], [2, 2, 5, 4]
#                       ,[2, 2, 5, 4], [2, 2, 5, 4], [2, 2, 5, 4], [2, 2, 5, 4]]))

print(solution(5, 6, [[1, 1, 2, 2], [1, 1, 2, 2], [1, 1, 2, 2], [1, 1, 2, 2]]))
