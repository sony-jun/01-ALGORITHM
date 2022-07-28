# 1223334444.....

srt, fin = map(int, input().split())

ls = []
for i in range(1,1001):
    for j in range(i):
        ls.append(i)
#print(ls) #[1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

sum_num = 0
for sum_ in ls[srt-1:fin]:  #3~7번까지니까 인덱스로 치면 2~6인데 뒤에는 자동으로 -1되니까
    sum_num += sum_
print(sum_num)