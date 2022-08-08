import sys

sys.stdin = open("블랙잭.txt")
n, m= list(map(int,input().split()))
card = list(map(int,input().split()))
max_total = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for z in range(j+1,n):            
            total = card[i] + card[j] + card[z]
            
            
            if max_total < total <=m :
                max_total = total
                
            if total == m:
                continue
print(max_total)
                
