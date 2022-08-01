T = int(input())

for i in range(T):
    x = input()
    stack = [x[0]]
    for j in range(1,len(x)):
        stack.append(x[j])
        if len(stack) >= 2 and stack[-2] == '(' and stack[-1] == ')':
            stack.pop()
            stack.pop()
    else:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')