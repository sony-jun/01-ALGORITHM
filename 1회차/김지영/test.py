result = []
while True:
    stc = input()
    stack = ['']

    if stc == '.':
        break
    for i in stc:
        print(i,stack)
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack[-1] == "(":
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == "[":
            stack.append(i)
        elif i == "]":
            if stack[-1] == "[":
                stack.pop()
            else:
                stack.append(i)
                break
    
    if len(stack) == 1:
        result.append("YES")
    else:
        result.append("NO")

for j in result:
    print(j)