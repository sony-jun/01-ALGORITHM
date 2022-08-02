# 9012
T = int(input())

for test in range(T):
    a = input()
    s = list(a)
    count_ = 0
    
    for i in s:
        if i == '(':
            count_ += 1
        elif i == ')':
            count_ -= 1
        if count_ < 0:
            print('NO')  
             
    if count_ > 0 :
        print('NO')
    elif count_ == 0: 
        print('YES')
        
