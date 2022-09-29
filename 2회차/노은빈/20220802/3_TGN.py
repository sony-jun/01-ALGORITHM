import sys
input = sys.stdin.readline

t = int(input())  #Test Case

for i in range(t):  #t만큼 반복
    r, e, c = map(int,input().split())
    
    if r + c < e :
        print('advertise')
    elif r + c == e:
        print('does not matter')
    else :
        print('do not advertise')
