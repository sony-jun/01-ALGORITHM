import sys
sys.stdin = open("11170.txt")
T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    cnt = 0
    for i in range(N, M+1):
        cnt += str(i).count('0')
    
    print(cnt)