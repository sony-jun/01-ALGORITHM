word = input()
croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
sum_word = 0

for i in croatia:
    if i in word:
        sum_word+=word.count(i)

print(len(word)-sum_word)
