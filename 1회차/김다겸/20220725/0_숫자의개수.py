# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

a = int(input())
b = int(input())
c = int(input())
# a*b*c를 문자열로 변환
mul = str(a * b * c)
# 9개의 숫자를 넣을 리스트를 0으로 초기화
ans = [0] * 10
# a*b*c의 문자열을 하나씩 순회
for i in mul:
    # 해당 숫자를 정수형으로 변경하여 ans의 인덱스에 넣어 값에 1씩 더함
    ans[int(i)] += 1

# 리스트 형태 없애고 개행해서 출력
print(*ans, sep='\n')