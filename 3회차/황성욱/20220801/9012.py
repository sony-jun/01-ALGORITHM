
n = int(input())
res = []
for i in range(n):
    stack = []
    ps = input()
    for j in ps:
        stack.append(j)
    if stack[0] == ')' or stack[-1] == '(':
        print('NO')
    elif stack.count('(') == stack.count(')'):
        print('YES')
    else:
        print('NO')


