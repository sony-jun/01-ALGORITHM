N = int(input())
cards = [i for i in range(1, N+1)]
discards = []

while len(cards) != 1:
    discards.append(cards.pop(0))
    cards.append(cards.pop(0))

for i in discards:
    print(i, end = ' ')
print(cards[0])