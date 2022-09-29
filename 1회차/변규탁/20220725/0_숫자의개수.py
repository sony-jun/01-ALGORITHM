# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

A = int(input())
B = int(input())
C = int(input())

number = str(A*B*C)

num_list = [0, 0, 0, 0, 0, 0, 0, 0, 4, 0]  # 0 ~  9 = 리스트 인덱스 자리수와 동일 (민석이문제)

for num in number: 
    num_list[int(num)] += 1

for num in num_list:
    print(num)


