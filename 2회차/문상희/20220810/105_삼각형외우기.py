angles = []
for i in range(3):
    angle = int(input())
    angles.append(angle)
if sum(angles) != 180:
    print('Error')
else:
    if len(set(angles)) == 1:
        print('Equilateral')
    elif len(set(angles)) == 2:
        print('Isosceles')
    else:
        print('Scalene')