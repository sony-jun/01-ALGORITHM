# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

A = int(input())
B = int(input())
C = int(input())

result = str(A * B * C)

# 곱한 값을 문자열로 변환해, 변환한 문자열을 반복문으로 순회
# 리스트의 인덱스에 해당되는 수가 된다면 
# 인덱스의 값을 +1 하는 형식

my_list = [0] * 10
for n in result:
    my_list[int(n)] += 1

# 0~9까지 수를 순회하여서 리스트의 인덱스와 값을 출력

for i in range(10):
    print(my_list[i])