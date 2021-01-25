first = "ACAYKP"
second = "CAPCAK"

f_list, s_list = [0] * 26, [0] * 26
for item in list(first):
    f_list[ord(item)-65] += 1

for item in list(second):
    s_list[ord(item)-65] += 1

print(f_list)
print(s_list)
answer = 0
for i in range(26):
    if f_list[i] != 0 and s_list[i] != 0:
        answer += min(f_list[i], s_list[i])

print(answer)
