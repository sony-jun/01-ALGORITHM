import sys

sys.stdin = open('균형잡힌세상_input.txt')


# 괄호를 받을 리스트들
small_left = '('
small_right = ')'
big_left = '['
big_right = ']'

left = []
right = []

while True:
    sen = input()
    for s in sen:
        if s == small_left:
            left.append(s)
        elif s == small_right:
            right.append(s)
        elif s == big_left:
            left.append(s)
        elif s == big_right:
            right.append(s)
        