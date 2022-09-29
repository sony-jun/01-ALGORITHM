import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    s = int(input()) # s :가격 t만큼 받기
    n = int(input()) # n : 옵션

    for _ in range(n):
        q, p = map(int,input().split())
        s += q * p  #가격은 q*n과 입력받은 s의 합     
        
    print(s)


    
