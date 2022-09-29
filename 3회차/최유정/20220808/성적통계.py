# https://www.acmicpc.net/problem/5800
K = int(input())
for k in range(1,K+1):
    N = list(map(int,input().split()))
    del N[0]
    n_max = max(N)
    n_min = min(N)
    N.sort(reverse=True)
    large_gap = 0
    for i in range(len(N)-1):
        if large_gap < abs(N[i]-N[i+1]):
            large_gap = abs(N[i]-N[i+1])
    print(f'Class {k}')
    print(f'Max {n_max}, Min {n_min}, Largest gap {large_gap}')
