# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")
n1,n2 = input().split(' ')
n1 = "".join(reversed(n1))
n2 = "".join(reversed(n2))
print(int(n1) if int(n1) > int(n2) else int(n2)) #if문 한 줄에 넣기. 큰 값 출력