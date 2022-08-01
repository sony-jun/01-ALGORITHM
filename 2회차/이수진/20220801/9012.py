N=int(input())

for _ in range(N):
    a=list(input())
    result=0
    for i in a:
        if result < 0 :
            break
        elif i == '(' :
            result += 1
        elif i==')':
            result -= 1
    
    print("YES" if result == 0 else "NO")