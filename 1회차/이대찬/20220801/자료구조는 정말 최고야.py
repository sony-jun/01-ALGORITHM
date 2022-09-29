import sys
from types import coroutine

sys.stdin = open('자료구조는 정말 최고야.txt')

N,M = map(int,input().split())
book_list = []
book_M_count = []
for i in range(M):
    book_M_count.append(int(input()))
    book_list.append(list(map(int,input().split())))
    
book_number = 1

result = []
while(len(result)<N):
    tmp =0
    # cnt가 없을때
    for book_M in book_list:
        if not book_M:
            continue
        if book_M[len(book_M)-1] == book_number:
            result.append(book_M.pop())
            book_number +=1
        else:
            tmp +=1
    if tmp == len(book_list):
        break
    
if len(result) == N:
    print("Yes")
else:
    print('No')
    
 

#==========================더미수 적을때
# while(lst1 and lst2):
#     if lst1[len(lst1)-1] == cnt:
#         result.append(lst1.pop())
#         cnt +=1
  
#     elif lst2[len(lst2)-1] == cnt:
#         result.append(lst2.pop())
#         cnt +=1
       
#     else:
#         print("No")
#         break
    
# if lst1:
#     while(lst1):
#         if lst1[len(lst1)-1] == cnt:
#             result.append(lst1.pop())
#             cnt +=1
#         else:
#             break
# elif lst2:
#     while(lst2):
#         if lst2[len(lst2)-1] == cnt:
#             result.append(lst2.pop())
#             cnt +=1
#         else:
#             break
            
# if len(result) == N:
#     print('Yes')

