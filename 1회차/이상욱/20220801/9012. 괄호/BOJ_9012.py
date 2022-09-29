import sys
sys.stdin = open ('9012.txt')

T = int(input())
right = 0
left = 0
for i in range(1, T+1):
    N = input()
    left = N.count('(')
    right = N.count(')')
    if left == right:
        print('YES')
    else:
        print('NO')

# list = list('(())())')

# print(list.pop(0))