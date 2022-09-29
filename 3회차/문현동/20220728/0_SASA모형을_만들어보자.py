# import sys
# sys.stdin = open("0_SASA모형을_만들어보자.txt", 'r')

s, a = map(int, input().split())

print(s // 2 if s // 2 <= a // 2 else a // 2)
# 두 변수를 2로 나눈 몫 중 작은 값이 모형을 만들 수 있는 최대 개수