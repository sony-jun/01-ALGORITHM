# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

a = int(input())
b = int(input())
c = int(input())

n = a * b * c
arr = [0 for i in range(10)]    # 0부터 9까지 0을 요소로 갖는 배열 생성

while n > 0:
    arr[n % 10] += 1            # n의 일의 자리부터 지워가며 개수를 더해줌
    n //= 10

for i in arr:                   # 숫자 배열 프린트
    print(i)
