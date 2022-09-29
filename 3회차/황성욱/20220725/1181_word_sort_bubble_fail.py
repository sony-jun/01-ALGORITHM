## 버블 - 시간초과
n = int(input())
word_dict = {}
for i in range(n):
    word = input()
    word_dict[word] = len(word)
print(word_dict)
res = sorted(word_dict, key = lambda x: word_dict[x])
for idx in range(len(res)):
    for j in range(len(res)-idx-1):
        if res[j] > res[j+1] and len(res[j]) == len(res[j+1]):
            res[j], res[j+1] = res[j+1], res[j]

for k in res:
    print(k)