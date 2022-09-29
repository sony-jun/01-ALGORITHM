T = int(input())

for i in range(T):
    
    n = int(input())
    options = int(input())
    
    for j in range(options):
        a, b = map(int, input().split())
        n += a*b

    print(n)