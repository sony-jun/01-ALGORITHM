#합계 21오바X, 가장큰수 만들기

import sys
sys.stdin = open("블랙잭.txt")

N, M = map(int,input().split()) #N:카드개수, M:초과하면안되는숫자
card_list = list(map(int,input().split()))

card_sum = 0

for a in range(N):
    for b in range(a+1,N):
        for c in range(b+1,N):
            abc = card_list[a] + card_list[b] + card_list[c]
            if abc <= M and abc > card_sum:
                card_sum = abc

print(card_sum)