import sys
sys.stdin = open('10101.txt')

numbers = [int(input()) for _ in range(3)]

if sum(numbers) == 180:
    if len(set(numbers)) == 1:
        print('Equilateral')
    elif len(set(numbers)) == 2:
        print('Isosceles')
    elif len(set(numbers)) == 3:
        print('Scalene')
else:
    print('Error')