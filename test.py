from itertools import combinations
items = ['1', '2', '3', '4']
for i in range(1, len(items)):
    data = list(map(''.join, combinations(items, i)))
    for item in data:
        print(list(item))
    print(data)
