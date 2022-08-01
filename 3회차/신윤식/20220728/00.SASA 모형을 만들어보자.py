# https://www.acmicpc.net/problem/23825

S_N, A_M = map(int,input().split())

# SASA모형에 S 2개, A 2개가 필요 이때, 정수로 나누어떨어져야함으로 몫만 계산
S = S_N // 2 
A = A_M // 2

# ex) 100 120 --->> 50 60(10) # 10개가 남음
# 더 작은 수를 출력
print(S) if S < A else print(A)