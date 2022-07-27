import sys
sys.stdin=input()
str_input=sys.stdin.lower()
str_diction={}
max=0
max_num=0
for i in str_input:
    if i not in str_diction:
        str_diction[i]=1
    else:
        str_diction[i]+=1
    if(str_diction[i]>max):
        max_num=i
        max=str_diction[i]
    elif str_diction[i]==max:
        max_num='?'
print(max_num)
