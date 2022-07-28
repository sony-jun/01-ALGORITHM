# https://www.acmicpc.net/problem/23825
import sys

sys.stdin = open("0_SASA 모형을 만들어보자.txt")

A, S = map(int, input().split())

A_ = A // 2                 #2
S_ = S // 2                 #2

print(min(A_,S_))






# # 1.시간 초과
# A, S = map(int, input().split())
# cnt = 0

# while A >= 2 and S >= 2:
#     A -= 2
#     S -= 2
#     cnt += 1

# print(cnt)
    
