import sys
sys.stdin = open('괄호.txt','r')

# )(

t = int(input())
 
for _ in range(t):
    a = input()
    stack_ = []
    
    for i in a:
        if i == "(":
            stack_.append(i)
        elif i == ")":
           
            if stack_:stack_.pop()
                
            else: 
                print('No')
                break
    else :
        if not stack_ :
            print('YES')
        else:
            print('NO')