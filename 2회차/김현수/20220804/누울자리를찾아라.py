import sys
sys.stdin = open('누울자리를찾아라.txt','r')

from pprint import pprint

N = int(input()) # N x N 정사각형 방 

seat = [list(input()) for _ in range(N)]
#pprint(seat)
wid = 0#누울자리가 있을까 
wid_x = 0 #누울자리가 있다 
for a in range(N):
    for b in range(N): #1개의 열에 N-1개의 표본이나옴
        if seat[a][b]  == '.': 
            wid += 1                        
        elif seat[a][b] == 'X':
            if wid > 1 :
                wid_x += 1
            wid =0  #들여쓰기를 주의하자
        
        if b == N-1 :
            if wid > 1 :
                wid_x += 1
            wid =0
leng = 0
leng_y = 0
for a in range(N):
    for b in range(N): 
        if seat[b][a]  == '.': 
            leng += 1                        
        elif seat[b][a] == 'X':
            if leng > 1 :
                leng_y += 1
            leng =0
        
        if b == N-1 :
            if leng > 1 :
                leng_y += 1
            leng =0

print(wid_x,leng_y)