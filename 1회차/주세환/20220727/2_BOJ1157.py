name = input().upper()

word_list = list(set(name))
name1 = []
for i in word_list:
    cnt = name.count(i)
    name1.append(cnt)
if name1.count(max(name1)) > 1:
    print('?')
else :
    max_index = name1.index(max(name1))
    print(word_list[max_index])
