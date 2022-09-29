

ch = [
        'zero','one','two','three','four',
        'five','six','seven','eight','nine'
] 
s = '"one4seveneight"'
for i in range(len(ch)):
    if ch[i] in s:
        answer = s.replace(ch[i],str(i))
        s = answer
re = int(s)
print(re)