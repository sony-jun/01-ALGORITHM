# 2480.
"""
이거랑 10101. 삼각형 외우기 문제 다시 풀어보기
"""
a, b, c = map(int,input().split())
if a == b == c:
    print(10000 + a * 1000)
elif a == b or b == c:
    print(1000 + b * 100)
elif a == c:
    print(1000 + a * 100)
else:
    print(max(a, b, c) * 100)