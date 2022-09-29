# 11652
"""
"""
import sys
sys.stdin = open("카드.txt")

N = int(input())
cards = {}
for _ in range(N):
    key = int(input())
    cards[key] = cards.get(key, 0) + 1

max_ = max(cards.values())
answer = []

for key in cards:
    if cards[key] == max_:
        answer.append(key)

answer = sorted(answer)
print(answer[0])