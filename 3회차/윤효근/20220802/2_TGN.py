import sys

sys.stdin = open("2_TGN.txt")

n= int(input())
for _ in range(n):
    ad = list(map(int,input().split()))
    if ad[0] < ad[1]-ad[2]:
        print('advertise')
    elif ad[0] == ad[1]-ad[2]:
        print('does not matter')
    elif ad[0] > ad[1]-ad[2]:
        print('do not advertise')
