
from itertools import count



A = set(map(int,input().split()))
B = set(map(int,input().split()))

print(len(A-B)+ len(B-A))

print(A^B)
print(len(A^B))
#A= list(map(int,input().split()))
#B= list(map(int,input().split()))
#rint(len(A-B)+ len(B-A)) #TypeError: unsupported operand type(s) for -: 'list' and 'list'
#리스트+리스트는 되는데 왜 리스트-리스트는 안 되는지 모르게ㅇ
# #print(A)
#rint(B)
#print(A+B)

#for i in Set_:
 #   if i not in memory:
  #      memory.append(i)
   # else:
      #  memory.remove(i)
       # print(memory)    
        

#for elem1 in A:
 #   if elem1 != A:
   #     list.append(elem1)
    #for elem2 in B:
     #   if elem2 != B:
     #      list.append()
  # print(len(list))