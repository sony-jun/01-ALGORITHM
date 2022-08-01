n = int(input())
stk = []
for i in range(2*n - 1):
    name = input()
    if name not in stk:
        stk.append(name)
    
    elif name in stk:
        stk.remove(name)

print(stk[0])
