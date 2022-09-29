N = int(input())

for a in range(N):
    r,e,c = list(map(int, input().split()))
    if e-c > r :
        print('advertise')
    if e-c == r :
        print('does not matter')
    if e-c < r :
        print('do not advertise')
    
