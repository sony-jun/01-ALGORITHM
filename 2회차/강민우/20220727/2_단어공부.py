N = input()
new = []
new_word = {}
count = 0
for a in N :
    if ord(a) >= 97:
        a = chr(ord(a)-32)       
        new.append(a)
    else : 
        new.append(a)

for a in new :
    if a in new :
        new_word[a] = new_word.get(a,0) + 1

max_word =  max(new_word.values())
result =[]

for a in new_word :
    if new_word[a] == max_word :
        result.append(a)

if len(result) > 1 :
    print('?')
else :
    print(result.pop())

    




