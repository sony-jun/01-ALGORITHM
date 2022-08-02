while True:
    T = str(input())
    stack = []
    for i in T:
        if i == '(' or '[':
            stack.append(i)
        elif i == ')' or ']':
            stack.pop
        
