from collections import deque
N = int(input())
participants = deque([])
winners = deque([])
loser = []

for _ in range(N):
    participants.append(input())

for _ in range(N-1):
    winners.append(input())

while len(participants) != 0:
    person_ = participants.popleft()
    if person_ in winners:
        winners.remove(person_)
    else:
        loser.append(person_)

print(*loser)