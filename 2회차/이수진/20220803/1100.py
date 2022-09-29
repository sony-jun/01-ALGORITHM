result=0
for _ in range(4):
    line=input()
    for i in range(0,7,2):
        if line[i]=='F':
            result+=1
    line=input()
    for i in range(1,8,2):
        if line[i]=='F':
            result+=1
print(result)
