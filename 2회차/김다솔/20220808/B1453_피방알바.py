import sys
sys.stdin = open('B1453.txt')
# print(seat)
guests = int(input())
want = list(map(int, input().split()))
occupied = []
ban = 0
for i in range(guests):
    if want[i] not in occupied:
        occupied.append(want[i])
    else: 
        ban += 1
  
print(ban)