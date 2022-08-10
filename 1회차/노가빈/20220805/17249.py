str = input()
count = 0
count2 = 0
for i in range(str.index('(')):
    if str[i] == '@':
        count += 1
for i in range(len(str)):
    if str[i] == '@':
        count2 += 1
print(count,count2-count,end=' ')
