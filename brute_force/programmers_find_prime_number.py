from itertools import permutations


def solution(numbers):
    n = len(numbers)
    data = list()
    for i in range(1, n+1):
        target = ''
        test = list(numbers)
        for item in permutations(test, i):
            s = ''
            for j in range(len(item)):
                s += item[j]
            target = target + s
            if len(target) == i:
                data.append(int(target))
                target = ''
    prime = set()
    for item in data:
        k = 1
        is_prime = True
        if item < 2:
            is_prime = False
        for k in range(2, item//2+1, k+k-1):
            if item % k == 0:
                is_prime = False
                break
        if is_prime:
            prime.add(item)
    return len(prime)


print(solution("123"))

# print(list(permutations(["1", "2", "3"], 3)))
