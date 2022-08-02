import sys
sys.stdin = open('B5063.txt')
T = int(input())
for tc in range(T):
    r, e, c = list((input().split()))
    if int(r) > int(e)-int(c):
        print('do not advertise')
    elif int(r) <int(e)-int(c):
        print('advertise')
    else:
        print('does not matter')