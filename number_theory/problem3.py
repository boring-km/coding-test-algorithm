1407
a, b = list(map(int, input().split()))
a -= 1

check_list = []

for s in range(99):
    check_list.append(pow(2, s))

answer = b
for i in range(1, 99):
    answer += (b // check_list[i]) * (check_list[i] - check_list[i-1])

for i in range(1, 99):
    answer -= (a // check_list[i]) * (check_list[i] - check_list[i-1])
answer -= a

print(answer)
