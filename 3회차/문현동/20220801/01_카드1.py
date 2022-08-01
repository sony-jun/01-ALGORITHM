import sys
'''
sys.stdin = open("01_카드1.txt", 'r')

from collections import deque

N = int(input())

bottom = []
cards = deque()
i = 0

for card in range(1, N + 1):
    cards.append(card)

while i < N - 1:
    bottom.append(cards.popleft())
    cards.append(cards.popleft())
    i += 1

print(' '.join(map(str, bottom + list(cards))))
'''
# 덱 풀이
###############################################
# 큐 풀이

N = int(input())

cards = []
bottom = []
i = 0

for card in range(1, N + 1):
    cards.append(card) # 1 2 3 4 5 6 7

while i < N - 1: # 5회 반복 
    bottom.append(cards.pop(0)) # 꺼내서 바닥에 놓고,
    cards.append(cards.pop(0)) # 맨 앞에서 꺼낸것을 다시 뒤로 보냄
    i += 1 # 5회까지 계속 반복


print(' '.join(map(str, bottom + cards)))