import sys
sys.stdin = open('TGN.txt')

N = int(input())

for i in range(N): 
    lst = list(map(int,input().split()))
    if lst[0] < lst[1] - lst[2]:
        print("advertise")
    elif lst[0] == lst[1] - lst[2]:
        print("does not matter")
    else:
        print("do not advertise")
    

 

