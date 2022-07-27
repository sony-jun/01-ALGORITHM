word = input()
word = word.upper()
c = 0
dic_word = {}
for i in word:
    if i in dic_word:
        dic_word[i] += 1
    else:
        dic_word[i] = 1
vl = [i for i in dic_word.values()]
# print(vl)
maxkey = max(dic_word,key=dic_word.get)

# if vl.count(dic_word[maxkey]) > 1:
#     print('?')
print(maxkey)
