N = int(input())
people = list(map(int, input().split()))
seat = {}

for a in people:
    seat[a] = seat.get(a, 0) + 1

cnt = 0
for a in people:
    if seat[a] > 1:
        cnt += 1
ct = 0
for a in seat.values():
    if a > 1 :
        ct += 1
print(cnt-ct) 

