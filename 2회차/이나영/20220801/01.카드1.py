from re import A
import sys

sys.stdin = open("01.카드.txt")


from collections import deque

N = int(input())
cards = deque(range(1, N+1))
res = []

# while문으로 cards에 카드가 남을 때까지 카드를 버리고, 
# 제일 아래로 옮기는 작업을 반복한다.

while cards: 
    card = cards.popleft()
    res.append(card)
    if cards:
        card = cards.popleft()
        cards.append(card)


print(*res) # *이거붙이면 []리스트에서 빠지는구나.
