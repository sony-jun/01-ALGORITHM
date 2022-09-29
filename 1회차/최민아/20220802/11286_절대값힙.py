import heapq
import sys
sys.stdin = open("20220802/11286_절대값힙.txt")
input = sys.stdin.readline

N = int(input())
num = []

for i in range(N):
    x = int(input())                    # 정수 x 입력받음

    if x > 0:                           # x가 양수일 때
        heapq.heappush(num, (x, x))     # num에 (절대값, 기본값) 추가
    
    elif x < 0:                         # x가 음수일 때
        heapq.heappush(num, (-x, x))    # num에 (절대값, 기본값) 추가
    
    else:                               # 입력으로 0이 주어졌을 때
        if not num:                     # 배열이 비어 있는 경우
            print(0)                    # 0을 출력
        else:
            n, m = heapq.heappop(num)   # num에서 가장 작은 원소를 n,m에 저장하고 pop
            print(m)                    # m을 출력 (n:절대값, m:기본값)