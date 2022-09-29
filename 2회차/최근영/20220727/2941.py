T = input()
word_list=['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt = 0
checking = 0
for i in range(0,len(word_list)):
    checking = T.count(word_list[i])
    if checking > 0 :
        cnt += checking
    T = T.replace(word_list[i],' ')

for j in T:
    if j != " ":
        cnt += 1
print(cnt)