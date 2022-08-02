# a, b = 5, 5
a, b = map(int, input().split())

if a > b:
    print('>')
elif a < b:
    print('<')
elif a == b:
    print('==')