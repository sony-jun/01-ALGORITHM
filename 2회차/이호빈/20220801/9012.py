T = int(input())

for i in range(T):
    stack = []
    a = int(input())
    for j in a:
        if j == "(":
            stack.append(j)
            print(stack)
        elif j == ")":
            if len(stack):
                stack.pop()
            else: #스택이 비었으면 "("가 없어 짝이 안 맞는다.
                print("NO")
                break
    else: #break문으로 끊기지 않고 수행됐을 경우 수행한다.
        if not stack: # break문으로 안 끊기고 스택이 비어있다면 괄호가 다 맞는거다.
            print("YES")
        else: #break안 걸렸더라도 스택에 괄호가 들어있다면 NO다. 
            print("NO")