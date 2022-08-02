# https://www.acmicpc.net/problem/9012

from queue import Empty


T = int(input())
list_ = []
for i in range(T):
    queue = list(input())
    for j in queue:
        if j == '(':
            list_.append(queue.pop(0))
           
        elif j == ')':
            if len(list_) == 0:
                print('NO')
                break
            else:
                list_.pop()
    else:
        if len(list_) == 0 :
            print('YES')
        else :
            print('NO')
    
    # print(queue)    
    # print(list_)
   
    
    
