from turtle import pen


a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a * 1000)
elif a != b != c:
    print(max[a, b, c] * 100)
else:
    print()