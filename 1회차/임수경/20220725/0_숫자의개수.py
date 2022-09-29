# https://www.acmicpc.net/problem/2577
from posixpath import split
import sys

sys.stdin = open("0_숫자의개수.txt")

# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 
# 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

# A, B, C = input() #오류

# result = list(str(A * B * C)) #오류

A = int(input())  # 각 A, B, C 를 int(input())
B = int(input())
C = int(input())

result = list(str(A * B * C))  #result 라는 변수에 각 곱한 결과를 형변환
for i in range(0, 10):  #for문을 사용하여 0~9까지의 범위로 설정 
    print(result.count(str(i)))  # count