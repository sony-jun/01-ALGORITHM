## 버블
from operator import le


n = int(input())
word_dict = {}
for _ in range(n):
    word = input()
    word_dict[word] = len(word)
print(word_dict)
res = sorted(word_dict, key = lambda x: word_dict[x])
