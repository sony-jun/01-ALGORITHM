# 직사각형 길이 찾기

T = int(input())

for i in range(1, T+1):
    a, b, c = map(int, input().split())
    for idx in range(T):
        if a == b and a != c:
            d = c
        elif a == c and a != b:
            d = b

        elif c == b and c != a:
            d = a
        elif a == b == c:
            d = a
        else:
            d = 'error'
    print(f'#{i}', d)