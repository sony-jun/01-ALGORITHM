a = input()

dic = {}
for i in a:
    if i.isupper() == False:
        i = i.upper()
    if i not in dic:
        dic[i] = 1
    else:     
        dic[i] = dic[i] +1

result = ''
max_= 0
for i in dic:
    if dic[i] > max_:
        max_ = dic[i]
        result = i
    elif dic[i] == max_:
        result = '?'
    
print(result)
 