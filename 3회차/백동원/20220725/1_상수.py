# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

A, B = input().split()          # 받은 숫자 입력값을 문자열로 할당한다.
list_A = list(map(int, A))      # 입력 받은 문자열을 하나씩 쪼개에 리스트에 할당한다.
list_B = list(map(int, B))
n = 0
result_A = 0
result_B = 0

for i in list_A:                # 거꾸로 뒤집기 위해서는 리스트 첫번째 숫자에 1, 두번째에 10, 세번째에 100 순서로 곱하여 모두 더한 수가 된다.
    result_A += (i * (10**n))
    n += 1

n = 0                           # n을 0으로 초기화

for i in list_B:
    result_B += (i * (10**n))
    n += 1

if result_A >= result_B:        # 뒤집은 숫자를 비교하여 더 큰 수 출력
    print(result_A)
else:
    print(result_B)