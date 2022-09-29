# https://www.acmicpc.net/problem/2908
a , b = map(int , input().split())

y = str(a)
y = y[::-1]
x = str(b)
x = x[::-1]

if int(x) > int(y) :
    print(x)
else:
    print(y)