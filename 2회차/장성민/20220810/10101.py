three = []
for _ in range(3):
    three.append(int(input()))

if sum(three) == 180:
    if three == 180:
        print('Equilateral')
    elif three[0] == three[1] or three[0] == three[2] or three[1] == three[2]:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')
