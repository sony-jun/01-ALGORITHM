# https://www.acmicpc.net/problem/2753

N = int(input())

#윤년이면
if N % 4 == 0 and N % 100 != 0 or N % 400 == 0:
    print(1)
else:
    print(0)