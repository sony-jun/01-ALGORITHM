word=input()
word=word.upper()
emp={}
for i in word:
    if i in emp:
        emp[i]+=1
    else: emp[i]=1
keys=[]
for key in emp:
    if max(emp.values())==emp[key]:
        keys.append(key)       
if len(keys)>=2:
    print('?')
else: print(keys[0])          
            
