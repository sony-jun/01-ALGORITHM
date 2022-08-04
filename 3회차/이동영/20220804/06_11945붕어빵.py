a, b = map(int, input().split())
m = []

for _ in range(a):
    str_ = list(input())
    str_.reverse()
    print(''.join(str_))