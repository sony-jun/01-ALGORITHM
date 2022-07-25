# https://www.acmicpc.net/problem/2908

# 세 자리 수 두 개를 입력
# 그 다음 크기가 큰 수를 출력
# 단, 수를 거꾸로 읽어 734와 893을 입력했다면
# 이 수를 437과 398로 읽어서 두 수중에 큰 수인 437을 출력
# 같지 않은 세 자리 수 두 개, 0이 포함되어 있지 않음

import sys

sys.stdin = open("1_상수.txt")

A, B = map(int, input().split())

# 입력 받은 숫자 A, B를 문자열로 바꾸어
# 끝에서부터 슬라이싱하고 다시 int 형변환
A_reverse = int(str(A)[::-1])
B_reverse = int(str(B)[::-1])

# if문을 사용하여 A_reverse가 B_reverse보다 크다면 A를 출력
if A_reverse > B_reverse:
    print(A_reverse)
# 그렇지 않다면 B_reverse를 출력
else:
    print(B_reverse)