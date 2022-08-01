import sys
from xml.etree.ElementTree import C14NWriterTarget

sys.stdin = open('괄호.txt')

N = int(input())

for i in range(N):
    lst = []
    tmp = []
    lst = list(input())

    while(lst):
        if not tmp:
            tmp.append(lst.pop())  #lst 마지막 pop 
            if not lst:
                break
            
        if lst[len(lst)-1] == tmp[len(tmp)-1]:
            tmp.append(lst.pop())
            
        else:
            lst.pop()
            tmp.pop()
    
    if not tmp:
        print("YES")
        continue
    else:
        print("NO")
        continue
                 
             
   