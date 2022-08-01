from collections import deque
n = int(input())

for i in range(n):
    VPS = deque(input())
    llst = []
    rlst = []
    if VPS[0] == ')' or VPS[-1] == '(':
        print('NO')
        continue
    while len(VPS) > 0:
        if VPS[0] == '(' and len(llst) >= len(rlst):
            llst.append(VPS.popleft())
        elif VPS[0] == ')' and len(llst) > len(rlst):
            rlst.append(VPS.popleft())
        else:
            rlst.clear()
            break
    if len(llst) == len(rlst):
        print('YES')
    else:
        print('NO')

             
