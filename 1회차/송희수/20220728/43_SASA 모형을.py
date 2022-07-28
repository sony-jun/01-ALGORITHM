#알파벳S 모양의 블록 N개와 알파벳A 모양의 블록 M개를 건졌다.
#{('S':'N'),('A':'M')}
import sys

sys.stdin = open("43_SASA 모형을.txt")
# N, M = map(int, input().split())

# if N//2 == M//2:
#     print(N//2)
# else:
#     print('')

N, M = map(int, input().split())

temp = min(N, M)

print(temp//2)
