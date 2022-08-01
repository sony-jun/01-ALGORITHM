
n = int(input())
res = []


for i in range(n):
    stack = []
    ps = input()
    for j in ps:
        stack.append(j)
    
    cnt = 0

    for k in range(len(stack)):
        for p in range(-len(stack), -1 + k, -1):
            if stack[k] == '(' and stack[p] == ')':
                cnt += 1
    
    print(cnt)

                
        

