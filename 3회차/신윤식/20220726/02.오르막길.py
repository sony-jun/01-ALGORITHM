# https://www.acmicpc.net/problem/2846

N = int(input())
P = list(map(int,input().split()))
lst = []

elevate = 0
for i in range(N-1): 
    if P[i] < P[i+1]:
        elevate += P[i+1]-P[i]
        lst.append(elevate)
    elif P[i] >= P[i+1]:
        elevate = 0
        
print(0) if len(lst) == 0 else print(max(lst)) 