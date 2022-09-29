# https://www.acmicpc.net/problem/2231

X = int(input())

for i in range(1, X + 1):
    Y = list(map(int, str(i)))
    Z = i + sum(Y)
    if Z == X:
        print(i)
        break

    if X == i:
        print('0')
