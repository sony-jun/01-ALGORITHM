l = []

for _ in range(3):
    l.append(int(input()))

if l.count(60) == 3:
    print("Equilateral")
elif sum(l) == 180:
    if len(set(l)) == 2:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")