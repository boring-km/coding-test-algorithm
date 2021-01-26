# def solution(words, queries):
#     answer = []
#     return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
pre = []
post = []

for item in queries:
    if item.find('?') == 0:
        post.append([item.rfind('?')+1, item[item.rfind('?')+1:], len(item)])
    else:
        pre.append([item.find('?'), item[0:item.find('?')], len(item)])

print(pre)
print(post)
answer = [0] * len(queries)
for i in range(len(pre)):
    for j in range(len(words)):
        if pre[i][1] == words[j][0:pre[i][0]] and len(words[j]) == pre[i][2]:
            answer[j] += 1
for i in range(len(post)):
    for j in range(len(words)):
        if post[i][1] == words[j][post[i][0]:] and len(words[j]) == post[i][2]:
            answer[j] += 1
print(answer)
