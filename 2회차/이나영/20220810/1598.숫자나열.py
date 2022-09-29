from re import A
import sys

sys.stdin = open("input1598.txt")

# for _ in range(4):
#     x1,y1 = map(int,input().split())

#반복문으로 돌리면 시간초과가 ?
#간단 사칙연산 같은데 // 개뿔...

a, b = map(int, input().split())


height = [1, 4, 3, 2]

# 높이
a_h = height[a%4]
b_h = height[b%4]

# 길이
if a % 4 == 0:
    a_w = a//4
else:
    a_w = a//4+1

if b % 4 == 0:
    b_w = b//4
else:
    b_w = b//4+1

print(abs(b_h-a_h)+abs(b_w-a_w))