import sys

sys.stdin = open("input.txt", "r")

t = int(input())

for tc in range(t):
    
    a ,b = map(int, input().split())
    
    m = [list(map(int, input().split())) for _ in range(a)]
    cnt = 0
    
    for i in range(b):
        level = a-1
        j = 0
        
        if m[a-1][i] == 1:
            level -= 1
            j += 1
            
        for k in range(j,a):
            if m[a-1-k][i] == 1:
               cnt += level - (a-1-k)   
               level -= 1
    print(cnt)
    
    