# https://jinho-study.tistory.com/379

import sys
sys.stdin = open('B10101.txt')

angles = [int(input()) for _ in range(3)]
# print(angles)
if sum(angles) == 180:
    if angles[0] == angles[1] or angles[0] == angles[2] or angles[1] == angles[2]:
        print('Isosceles')
    elif angles[0] == angles[1] == angles[2]:
        print('Equilateral')
    else:
        print('Scalene')
else:
    print('Error')