import sys

sys.stdin = open("2_괄호.txt")

n = int(input())
for i in range(n):
    s = input()
    sum = 0

    s_list = []
    for ele in s:
        if ele == '(':
            sum += 1
        elif ele == ')':
            sum -= 1
        if sum <0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    else:
        print('YES')