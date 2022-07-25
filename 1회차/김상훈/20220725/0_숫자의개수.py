# https://www.acmicpc.net/problem/2577
import sys
sys.stdin = open("0_숫자의개수.txt")

a = int(input()) #줄을 바꿔가면서 입력을 받으므로
b = int(input()) #한줄마다 input()
c = int(input())

# 17037300 = 1,7,0,3,7,3,0,0 이므로 문자열로 변환해서 count함수로 갯수를 세는 방향으로 접근

d = str(a*b*c) # str함수를 이용하여 문자열로 변환.
for i in range(10): # 총 세야 할 것이 0~9이므로 range(10-1)
    print(d.count(str(i))) #  count 함수 이용해서 갯수 카운트
