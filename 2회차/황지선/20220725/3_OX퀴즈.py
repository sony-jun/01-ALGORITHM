# https://www.acmicpc.net/problem/8958
# 8958번 OX 퀴즈

n= int(input())

for i in range(n):
    a= input()
    b= list(a)
    sum = 0
    x = 1

    for i in b:
        if i == 'O':
            sum += x
            x += 1
        else:
            x = 1
    print(sum)