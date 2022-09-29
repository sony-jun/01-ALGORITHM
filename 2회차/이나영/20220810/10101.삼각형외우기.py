#세 각의 크기가 60이면 equilateral
#세 각의 크기가 180이고 두 각이 같을 때에는 isosceles
#세 각의 합이 180이고 같은 각이 없을 때에는 scalane
#세 각의 크기가 180이 아닌 경우에는 error.
from re import A
import sys

sys.stdin = open("input10101.txt")


a = int(input())
b = int(input())
c = int(input())

if a == b == c == 60:
    print('Equilateral')
elif a+b+c == 180 and (a==b or b==c or a==c):
    print('Isosceles')
elif a+b+c == 180:
    print('Scalene')
else :
    a + b + c != 180
    print("Error")






