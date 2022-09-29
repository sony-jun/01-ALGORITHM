# https://www.acmicpc.net/problem/10101

a = int(input())
b = int(input())
c = int(input())
result = ''

if (a + b + c) == 180:
    if a == 60 and b == 60 and c == 60:
        result = 'Equilateral' 
    elif (a == b) or (b == c) or (a == c):
        result = 'Isosceles'
    elif (a != b) and (b != c)and (a != c):
        result = 'Scalene'
else:
    result = 'Error'
print(result)