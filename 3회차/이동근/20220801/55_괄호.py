N = int(input())

for _ in range(N):
    vps = input()
    stack = []

    for ch in vps:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if not stack:
                stack.append(ch)
            elif stack[-1] == '(':
                stack.pop()

    print("NO" if stack else "YES")

# https://www.acmicpc.net/source/46994903
# 굉장히 좋은 풀이
# T = int(input())

# for i in range(T):
#     vps = input()
    
#     while "()" in vps:
#         vps = vps.replace("()", "")
    
#     if vps:
#         print("NO")
#     else:
#         print("YES")