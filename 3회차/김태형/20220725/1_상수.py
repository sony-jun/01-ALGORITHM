# https://www.acmicpc.net/problem/2908

N, L = map(int,input().split())
for i in N:
    D,R,G = map(int,input().split())
time=0
if D<R:
    time+=(R-D)+G
else:
    time+=D+G

print(time)