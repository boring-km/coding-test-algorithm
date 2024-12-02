# 14232 나의 제출
n = int(input())

limit = n ** 0.5 + 1

answers = []

def get_numbers(number):
    count = 2
    check = False
    while count <= limit + 1:
        if number % count == 0:
            answers.append(count)
            check = True
            get_numbers(int(number/count))
            break
        else:
            count += 1
    if not check and number != 1:
        answers.append(number)

get_numbers(n)
answers.sort()
print(len(answers))
print(*answers)

# 코드 최적화 및 재귀함수 없앤 버전

n = int(input())

limit = n ** 0.5 + 1

answers = []

limit = int(n ** 0.5) + 1
for count in range(2, limit + 1):
    while n % count == 0:
        answers.append(count)
        n //= count
if n != 1:
    answers.append(n)

answers.sort()
print(len(answers))
print(*answers)