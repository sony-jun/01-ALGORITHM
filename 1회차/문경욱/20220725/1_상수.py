# https://www.acmicpc.net/problem/2908
# 두 수 A,B에 입력받음
A, B = map(int, input().split())
# 거꾸로 뒤집을 변수 rev_A와 rev_B를 선언
rev_A, rev_B = 0, 0

while A:
    #이전 결과에 10을 곱하고
    rev_A *= 10
    # 나머지를 더해주고
    rev_A += A %10
    # number를 깍는다.
    A //=10

while B:
    #이전 결과에 10을 곱하고
    rev_B *= 10
    # 나머지를 더해주고
    rev_B += B %10
    # number를 깍는다.
    B //=10

#rev_A와 rev_B중 더 큰 값 출력
print(rev_A if rev_A > rev_B else rev_B)
