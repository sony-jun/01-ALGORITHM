# https://www.acmicpc.net/problem/2231
import sys

sys.stdin = open("2231.txt")
N = int(input())
result = 0
for i in range(1, N+1): # i는 1부터 N까지의 숫자
    num = list(map(int, str(i))) # int는 iterable하지 않아서 list(i)로 작성할 수 없음.
    result = i + sum(num)
    if result == N:
        print(i)
        break
    
    if i == N: # 생성자가 없을 때 ex) 1, 3
        print(0)
