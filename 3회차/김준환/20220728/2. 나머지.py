text = input().upper()
dic={}
for t in text:
    if t in dic:
        dic[t] += 1
    else:
        dic[t] = 1
value=0
for i in dic:
    if dic[i] > value:
        value=dic[i]
        for k in dic:
            if dic.get(k) == value:
                answer=k
    elif dic[i] == value:
        answer = '?'
print(answer)