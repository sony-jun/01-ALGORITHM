# https://www.acmicpc.net/problem/2161
import sys

sys.stdin = open("0_카드1.txt")

from collections import deque

N = int(input())                        # 
N_1 = range(1,N+1)                      # 1~7까지
list_1 = deque(N_1)


while len(list_1) > 1 :                 # 하나 남을때 까지 반복
    print(list_1.popleft(), end = ' ')  # list_1[0]을 출력
    list_1.append(list_1.popleft())     # list_1[-1]을 list_1[0]으로 옮김
print(*list_1)                          # 남은거 프린트


    
