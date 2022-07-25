# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")
num1, num2 = input().split()
#역순으로 나오게 하기
num1 = int(num1[::-1]) 
num2 = int(num2[::-1])
# if문을 통해 num1이 클때 num1을뽑고 아니면 num2를뽑는다.
if num1 > num2:
    print(num1)
else :
    print(num2)