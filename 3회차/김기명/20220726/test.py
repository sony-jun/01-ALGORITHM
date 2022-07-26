point = 0
winner = 0
point2 = 0

for i in range(5):
    point = sum(map(int,input().split()))
    if point2 > point:
        point2 = point
        winner = i + 1
print(point2, winner)
