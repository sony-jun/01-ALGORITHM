# https://www.acmicpc.net/problem/9325
T = int(input()) #테스트 케이스
for t in range(T):
    s = int(input()) #자동차 가격
    n = int(input()) #옵션 개수
    total = s
    for i in range(n):
        p, q = map(int,(input().split())) #개수, 가격
        option = p*q
        total += option
    print(total)