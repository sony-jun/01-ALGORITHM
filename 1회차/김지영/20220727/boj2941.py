# import re
cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
word = input()
sum = 0
for i in range(len(cro)):
    # print(word,cro[i])
    c = word.count(cro[i])
    # print(c)
    word = word.replace(cro[i],' ')
    # print(word)
    sum += c
word = word.replace(' ','')
print(sum+len(word))
# print(re.sub(cro[5],'',word))   # 이건 작동을 하는데...
print(word)