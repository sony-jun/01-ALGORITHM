
n = int(input())
res = []


for i in range(n):
    stack = []
    ps = input()
    cnt = 0
    for j in range(len(ps)):
        if ps[j] == '(':
            stack.append(ps[j])
            cnt += 1
        
        elif ps[j] == ')' and cnt > 0:
            stack.append(ps[j])
            cnt -= 1

    if stack.count('(') == stack.count(')') and len(stack) == len(ps):
        print('YES')
    else:
        print('NO')

        
        
            
    
    
                
        

