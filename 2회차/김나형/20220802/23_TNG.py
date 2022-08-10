import sys

sys.stdin = open("23_TNG.txt")

T = int(input())
for _ in range(T):
    ad = list(map(int, input().split()))
    if ad[0] < ad[1]-ad[2]:
        print('advertise')
    elif ad[0] == ad[1]-ad[2]:
        print('does not matter')
    else:
        print('do not advertise') 
