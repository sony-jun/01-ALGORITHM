n = int(input())

for i in range(1,n+1):
    str_ = input()
    str_ = str_.replace('()','')
    
    
    while 1:
        if str_.count('()') != 0:
            str_ = str_.replace('()','')

        else:
            break 
    
    if len(str_) != 0 :
        print('NO')
    
    else:
        print('YES')