#카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는.
#target값 M을 외친다. 
# N장의 카드에서 3장의 카드를 고르되 M의값을 넘지않고 최대한 가깝게. 
# 
from sys import stdin

import sys

daf blackjack(n,m cards):
max_total = 0
n,m = input().split()
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            total = cards[i] + cards[j] + cards[k]
            
            if max_total < total <= m:
                max_total = total
                
            if total == m:
                return total

return max_total