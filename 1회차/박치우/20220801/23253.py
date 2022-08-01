from collections import deque

N, M = map(int,input().split())
lst = [num for num in range(1,1+N)]
dummy_lst = []
dummy_num = []
for i in range(M):
    dummy_num.append(int(input()))
    dummy_lst.append(input().split())

new_lst = []
for j in dummy_num:
    for k in range(j):
        for s in range(j):
            new_lst.append(dummy_lst.pop(dummy_lst[k][s]))
sum = 0
for i in range(len(lst)):
    sum += lst - new_lst
if sum == 0 :
    print('Yes')
else:
    print('No')

    
