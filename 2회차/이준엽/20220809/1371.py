sentence = []
chr_num = [0 for i in range(26)]
result = []
while True:
    try:
        sen = input()
        sentence.append(sen)
    except:
        break
for s in sentence:
    for cr in s:
        if cr in 'abcdefghijklmnopqrstuvwxyz':
            chr_num[ord(cr)-97]+=1
max_cnum = max(chr_num)
for i in range(26):
    if chr_num[i] == max_cnum:
        result.append(chr(i+97))
print(*result,sep='')