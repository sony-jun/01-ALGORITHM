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


n , m = map(int,input().split()) # 최댓값 카드 갯수 받기

cards = list(map(int,input().split())) #카드 값 받기

_max = 0 # 최대값을 비교하면서 저장

for i in range(0,n-2): #카드 3개기 때문에 카드 숫자 - 2까지
    if _max == m:
        break

    for j in range(i+1,n-1): # 2번째 카드는 [1번째 카드번호 + 1] 부터 카드 숫자-1 까지
        if _max == m:
            break

        for k in range(j+1,n): # 3번째 카드는 [2번째 카드번호 + 1] 부터 카드 숫자-1 까지
           
            tmp = cards[i] + cards[j] + cards[k] # 카드 세개 합 저장
            
            if m > tmp > _max:
                _max  = tmp
            
            elif tmp  == m:
               _max  = tmp
               break

print(_max)
