T = int(input())
for test_case in range(1 , T + 1):
    mat = []
    s = int(input())
    n = int(input())
    y = 0
    
    for i in range(n):
        q , p = map(int , input().split())
        y = y + q * p
    print(s + y)
        