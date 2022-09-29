# # 창영이는 삼각형의 종류를 잘 구분하지 못한다. 따라서 프로그램을 이용해 이를 외우려고 한다.

# 삼각형의 세 각을 입력받은 다음, 

# 세 각의 크기가 모두 60이면, Equilateral
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
# 세 각의 합이 180이 아닌 경우에는 Error
# 를 출력하는 프로그램을 작성하시오.



a = int(input())
b = int(input())
c = int(input())

if a == b == c == 60:               # 세 각의 크기가 모두 60인 경우
    print("Equilateral")
elif a + b + c == 180:              # 세 각의 합이 180이고
    if a == b or b == c or c == a:  # 두 각이 같은 경우
        print("Isosceles")
    else:                           # 같은 각이 없는 경우
        print("Scalene")
else:                               # 세 각의 합이 180이 아닌 경우
    print("Error")


# a=int(input())
# b=int(input())
# c=int(input())

# if a == 60 and b == 60 and c == 60:
#     print("Equilateral")
# if a+b+c ==180: 
#     if a==b or b==c or c==a :
#         print("Isosceles")
# if a+b+c ==180: 
#     if a!=b!=c:
#         print("Scalene")
# if a+b+c!=180:
#     print("Error")
