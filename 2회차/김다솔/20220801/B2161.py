from collections import deque
N = 7

og_list = []
new_list = []
for i in range(1, N+1):
    og_list.append(i)
og_list = deque(og_list)
print(og_list)

# N = int(input())
# cards = deque(list(range(1, N+1)))
# discard = []
# while True:
#     discard.append(cards.popleft())
#     cards.append(cards.popleft())
#     if len(cards) == 1:
#         print(*discard, cards[0])
#         break

n = int(input())
cards = list(range(1, n+1))
discard = []
while len(cards) > 1:
    discard.append(cards[0])
    cards = cards[2:] + [cards[1]]

print(*discard, cards[0])