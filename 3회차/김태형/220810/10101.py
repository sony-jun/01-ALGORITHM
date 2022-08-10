# 삼각형의 세 각을 입력받은 다음, 삼각형의 종류를 구분하는 문제

a = int(input())
b = int(input())
c = int(input())
sum_angle = a+b+c

if a==60 and b==60 and c==60:
    print("Equilateral")
elif sum_angle==180:
    if a==b or b==c or c==a:
        print("Isosceles")
    elif a!=b and b!=c and c!=a:
        print("Scalene")
else:
    print("Error")
