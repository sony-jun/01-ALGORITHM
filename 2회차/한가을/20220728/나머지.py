# 백준 3052
# 자연수 A와 B가 있을 때 A % B는 A를 B로 나눈 나머지
# 수 10개를 입력받고 이를 42로 나눈 나머지를 구한다.
# 그 다음 서로 다른 값이 몇 개 있는지 출력

import sys

# input = sys.stdin.readline
sys.stdin = open('나머지.txt', 'r')

remainder_ = []

for num in range(10):
    num = int(input())
    remainder_.append(num % 42)
remainder_ = set(remainder_)
print(len(remainder_))