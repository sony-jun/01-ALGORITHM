import sys

sys.stdin = open("2_괄호.txt")

n = int(input())
for i in range(n):
    s = input()
    sum = 0


    for ele in s:
        if ele == '(':
            sum += 1
        elif ele == ')':
            sum -= 1
        if sum <0: #')'가 '(' 보다 많은경우 끝까지 검사할 필요가 없다
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum ==0:
        print('YES')

