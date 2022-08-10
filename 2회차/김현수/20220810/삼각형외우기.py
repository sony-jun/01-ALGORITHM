import sys
sys.stdin = open("삼각형외우기.txt")

num = [int(input()) for _ in range(3)]
#print(num)
num_sum = sum(num)
if num_sum == 180:
    if num[0] == num[1] == num[2]:
        print('Equilateral')
    elif num[0] != num[1] and num[1] != num[2] and num[2] !=  num[0]:
        print('Scalene')
    else:
        print('Isosceles')
else:
    print('Error')