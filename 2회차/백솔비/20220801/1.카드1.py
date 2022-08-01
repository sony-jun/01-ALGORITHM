import sys
sys.stdin = open("1.카드1.txt")

card = []
N = int(input())

for i in range(1, N+1):
    card.append(i)

while len(card) != 1:
    # 앞에서부터 순서대로 빠짐
    print(card.pop(0))
    card.append(card.pop(0))

print(*card)