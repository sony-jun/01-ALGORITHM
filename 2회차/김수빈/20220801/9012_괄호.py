T = int(input())

for i in range(T):
    stack = []
    vps = list(input())
    for j in vps:
        if j == '(':
            stack.append(j)
        if j == ')':
            if len(stack) != 0:
                stack.pop()

    if len(stack) == 0:
        print('YES')
    else:
        print('NO')