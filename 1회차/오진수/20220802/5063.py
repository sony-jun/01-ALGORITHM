words = int(input())

for i in words:

    if words.index(1) - words.index(2) > words.index(0):
        print("advertise")
    elif words.index(1) - words.index(2) == words.index(0):
        print("does not matter")
    elif words.index(1) - words.index < 0 :
        print("do not advertise")

N = int(input())
for _ in range(N):
    r, e, c = map(int, input().split())
    if e - c < r :
        print("do not advertise")
    elif e - c == r:
        print("does not matter")
    else:
        print("advertise")
=

N=int(input())
#r 그냥수익
#e 광고하고 수익
#c 광고비
for i in range(1,N+1):
    r,e,c=map(int,input().split())
    if e-c > r:
        print("advertise")
    elif e-c ==r:
        print("does not matter")
    elif e-c <r:
        print("do not advertise")



    d = b - c
    if a > d:
        print("do not advertise")
    elif a < d:
        print("advertise")
    else:
        print("does not matter")