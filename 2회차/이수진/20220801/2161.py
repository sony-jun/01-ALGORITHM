n=int(input())
nl=[]
for i in range(1,n+1):
    nl.append(i)
while len(nl) != 1 :
    print(nl.pop(0),end=' ')
    nl.append(nl.pop(0))
print(nl[0])



from collections import deque

N = int(input())
card = deque(list(range(1, N+1)))

out = []

while card:
    
    card_pop = card.popleft()
    out.append(card_pop)

    if card:
        card_pop = card.popleft()
        card.append(card_pop)

print(*out)