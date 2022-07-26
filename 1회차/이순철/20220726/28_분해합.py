# https://www.acmicpc.net/problem/2231
import sys

sys.stdin = open("28_분해합.txt")
#입력
a = int(input())
#연산
for i in range(1, a+1):
    hap = i + sum(map(int, str(i)))
    if hap == a:
        print(i)
        break
    if i == a:
        print(0)

        


