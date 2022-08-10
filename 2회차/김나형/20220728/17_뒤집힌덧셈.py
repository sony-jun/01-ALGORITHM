

import sys
sys.stdin = open("17_뒤집힌덧셈.txt")

x, y = map(int, input().split())

Rev_x = int(str(x)[::-1])
Rev_y = int(str(y)[::-1])

Rev_sum = int(str(Rev_x + Rev_y)[::-1])
# 출력 값이 01이 나오지 않기 위해 int로 바꿔야한다.
print(Rev_sum)