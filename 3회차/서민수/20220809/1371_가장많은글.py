from itertools import count


word = input()
count_ = list(set(input(word)))
a = []

for i in count_:
    cnt = word.count(i)
    a.append(cnt)
print(a)