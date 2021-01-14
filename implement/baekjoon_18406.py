# 4분 29초
n = input()
size = len(n)
mid = int(size/2)
front = [int(i) for i in n[0:mid]]
back = [int(i) for i in n[mid:size]]

if sum(front) == sum(back):
    print('LUCKY')
else:
    print('READY')