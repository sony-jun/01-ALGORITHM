n = input()
dic = {}
max = -9999
n = n.upper()
count = 0
for i in n:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
for j in dic:
    if dic[j] > max:
        max = dic[j]
for k in dic:
    if dic[k] >= max:
       count += 1
       big = k
if count >= 2:
    print('?')
else:
    print(big)
        

        
