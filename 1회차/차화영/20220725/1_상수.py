# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")
a, b = input().split()
# 문자열을 슬라이싱을 할 것이기 때문에 map(int, )를 사용하지 않았음
back_ab = [a[::-1], b[::-1]]
# a와 b 각각을 거꾸로 하여 back_ab라는 리스트에 담는다.
n = sorted(back_ab, reverse= True)
# back_ab를 sorted 함수를 이용하여 내림차순으로 정렬
print(n[0])
# 리스트에서 인덱스가 0인 첫번째 숫자가 더 크다.