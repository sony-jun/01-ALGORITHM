# import sys

# sys.sydin = open('TGN_input.txt')

N = int(input())

cnt = 0

while cnt != N:
    r, e, c = map(int, input().split())
    
    if r < e - c:
        print('advertise')
    elif r > e - c:
        print('do not advertise')
    else:
        print('does not matter')
    
    cnt += 1