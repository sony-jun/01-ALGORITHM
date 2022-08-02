n = int(input())

for _ in range(n) :
    a = int(input())
    a1 = set(map(int, input().split()))
    
    m = int(input())
    a2 = list(map(int, input().split()))

    for j in a2 :
        if j in a1 :
            print(1)
        else :
            print(0)