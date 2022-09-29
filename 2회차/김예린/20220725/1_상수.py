# https://www.acmicpc.net/problem/2908
import sys

a, b = map(str, input().split())
back_a = ''
back_b = ''

for i in range(len(a)-1, -1, -1): # range() 역순(-1)을 사용한다. 
    back_a += a[i]                # 역순된 a 값을 back_a에 차례대로 넣어준다.
for j in range(len(b)-1, -1, -1):
    back_b += b[j]

if back_a > back_b:               # 만약 역순된 a가 더 크다면,
    print(back_a)                 # back_a를 출력하고,
else:                             # 역순된 b가 더 크다면,
    print(back_b)                 # back_b를 출력한다. 

sys.stdin = open("1_상수.txt")
