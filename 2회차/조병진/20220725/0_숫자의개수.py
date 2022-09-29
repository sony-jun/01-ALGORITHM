# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

# 각 줄의 자연수 입력
A = int(input())
B = int(input())
C = int(input())

# 각 자릿수를 담을 리스트 박스
number = [0] * 9
# 곱한 결과를 리스트, 문자 형태로 변환
result = list(str(A * B * C))

# 각 자릿수를 반복하여 해당 인덱스에 1씩 추가
for i in result:
    number[int(i)] += 1
# 한 줄씩 출력
for i in number:
    print(i)
