# 창영이는 삼각형의 종류를 잘 구분하지 못한다. 따라서 프로그램을 이용해 이를 외우려고 한다.

# 삼각형의 세 각을 입력받은 다음, 

# 세 각의 크기가 모두 60이면, Equilateral
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
# 세 각의 합이 180이 아닌 경우에는 Error
# 를 출력하는 프로그램을 작성하시오.




a = [int(input()) for _ in range(3)]

# a안에 숫자가 180일때
if sum(a) == 180:
    # a[0] a[1] [2]가 다같다면 
    if a[0] == a[1] == a[2]:
        print("Equilateral")
        # a[0] a[1] a[2]가 두개만 같다면
    elif a[0] == a[1] or a[1] == a[2] or a[2] == a[0]:
        print('Isosceles')
        # 전부 다 다르면
    elif a[0] != a[1] != a[2]:
        print("Scalene")
# 180이 아니라면
else:
    print("Error")