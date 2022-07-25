# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")
#입력 값 거꾸로 비교하고
#출력

A, B =map(int, input().split())

A=A
compare1=(A//100) + (((A% 100)// 10)*10) +((A% 10)*100)

B=B
compare2=(B//100) + (((B% 100)// 10)*10) +((B% 10)*100)
#거꾸로
if compare1>compare2:
    print(compare1)
else:
    print(compare2)