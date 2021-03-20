# https://alpyrithm.tistory.com/100
data = input()
alpha_list = [0 for _ in range(26)]

for s in data:
    alpha_list[ord(s) - 65] += 1

odd = 0
odd_string = ''
string = ''

for i in range(26):
    if alpha_list[i] % 2 == 1:  # 두개씩 있어야 짝이 되는데 하나만 나오면 위험
        odd += 1
        odd_string += chr(i+65)
    string += chr(i+65) * (alpha_list[i] // 2)

if odd >= 2:
    print("I'm Sorry Hansoo")
else:
    print(string + odd_string + string[::-1])


