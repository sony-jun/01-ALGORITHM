import sys
input = sys.stdin.readline

N, M = map(int,input().split())

flag  = True #???
for i in range(M): 
    num = int(input())
    book_list = list(map(int,input().split()))
    for j in range(num-1):
        if book_list[j] < book_list[j+1]:
            flag = False
            break
    if not flag : 
        break
print('Yes' if flag else 'No') 