T = int(input())                                    # PS (Parenthesis String)
                                                    # VPS (Valid Parenthesis String)
for i in range(T):
    stack = []
    VPS = input()
    
    for PS in VPS :  # check every 'PS(string)' in 'VPS'
       
        if PS == '(': # If 'PS' is '(' the, add to list 'stack[]'
            stack.append(PS)
        
        elif PS == ')': # If 'PS' is ')' then pop it.
            if stack:
                stack.pop()
            
            else: # If there is no PS in VPS, then print 'no'
                print("NO")
                
                break
    
    else: # break문으로 끊기지 않고 수행됬을경우 수행한다
        
        if not stack: # break문으로 안끊기고 스택이 비어있다면 괄호가 다 맞는거다.
            print("YES")
        else: # break안 걸렸더라도 스택에 괄호가 들어있다면 NO이다.
            print("NO")


