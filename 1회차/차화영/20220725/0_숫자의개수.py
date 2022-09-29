# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")
a = int(input())
b = int(input())
c = int(input())
product = list(str(a*b*c))
# str으로 형변환하여 한 글자씩 끊어서 리스트로 바꾼다. int는 not iterable하기 때문.

number = list(map(int, product))
# 리스트 안에 각 요소가 ['1', '7']와 같은 str이므로 각각을 숫자로 바꿔 그 개수를 세기 위해 map을 사용한다.

for i in range(0, 10):
    # i는 0부터 9까지
    if len(number) ==0:
        print(0)
        # number의 길이가 0이면 즉, i에 해당하는 숫자가 number에 없으면 0을 출력
    else:
        print(number.count(i))
        # 그렇지 않으면 number 리스트의 요소 i의 개수를 출력