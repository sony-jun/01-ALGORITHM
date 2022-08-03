import sys
from unittest import result

sys.stdin = open("input.txt", "r")

list_ = []
n, m = map(str,input().split())

result_list = []

list_.append(list(n))
list_.append(list(m))

for i in list_ :
    for j in i:
        if j == '6':
            i[i.index(j)]  = '5'
result = 0           
for i in list_:
    str_ = ''
    for j in i:
       str_ += j
    
    result += int(str_)
result_list.append(result)
result = 0
for i in list_ :
    for j in i:
        if j == '5':
            i[i.index(j)]  = '6'
           
for i in list_:
    str_ = ''
    for j in i:
       str_ += j
    
    result += int(str_)
result_list.append(result)

for i in result_list:
    print(i,end=' ')
