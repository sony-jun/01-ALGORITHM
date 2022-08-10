#백준 삼각형 외우기 101010

A = int(input())
B = int(input())
C = int(input())


if A+B+C == 180:
    if A == B == C:
        print('Equilateral')
    elif A == B or A == C or B == C:
        print('Isosceles')
    elif A != B and A != C and B != C:
        print('Scalene')
else:
    print('Error')