N = 1041
binary_number = format(N, 'b')
binary = str(format(N, 'b'))

end = -1

for i in range(len(binary)-1, -1, -1):
    if binary[i] == '1':
        end = i
        break

new_binary = binary[1:end].split('1')
new_binary.sort()

result = len(new_binary[-1])

print(result)
