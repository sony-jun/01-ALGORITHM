# https://www.acmicpc.net/problem/9455
import sys

sys.stdin = open("2_박스.txt")

input = sys.stdin.readline

for i in range(int(input())):
    m, n = map(int, input().split())
    case = [list(map(int, input().split())) for _ in range(m)]
    ans = 0  
    
    for j in range(n):
        cnt = 0
        for k in range(m):
            if case[k][j]:
                cnt += 1 
            else:
                ans += cnt  
    print(ans)