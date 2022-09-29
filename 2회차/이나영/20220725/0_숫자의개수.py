# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

# count 함수를 사용하기 위해, int가 아닌 str형태로 바꾼 뒤 출력

num1 = int(input())
num2 = int(input())
num3 = int(input())
result = list(str(num1 * num2 * num3))  
# list는 str.int개체는 반복할 수 없으니까.int개체는 반복할 수 없다.str으로!

# 정수(int)끼리 곱한 값을 문자열(str)로 바꾼 뒤 list함수를 이용해서 리스트화.
# [1, 7, 0, 3, 7, 3, 0, 0]

for i in range(10):           # i = 0 ~ 9
    print(result.count(str(i))) # i를 문자열(str)로 바꿔서 몇 개 있는지 count함