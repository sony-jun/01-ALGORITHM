from functools import total_ordering
from tracemalloc import start


n = int(input())
l = list(map(int,input().split()))
gap = 0

startpoint = -1
gap = []

for i in range(1,len(l)):
    gap.append(l[i]-l[i-1])

total = 0
Max = 0

for i in range(0,len(gap)):
    if gap[i] > 0:
        total+=gap[i]

        if total > Max:
            Max = total
    else:
        total = 0
        

print(Max)


    

    
    