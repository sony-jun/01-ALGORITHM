# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("input.txt")
# abc를 차례로 받아준다.
a = int(input())
b = int(input())
c = int(input())
# str 함수를 이용하여 문자열로 변환하고, 리스트를 이용하여 각각의 문자를 각요소 리스트로 변환한다.
result = list(str(a*b*c))
# 이 후 카운트하여 리스트에 몇개씩 있는지 프린트
for i in range(10):
    print(result.count(str(i)))
