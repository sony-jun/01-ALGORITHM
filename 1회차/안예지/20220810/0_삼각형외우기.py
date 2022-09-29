# 10101.

""" 
접근방법
1. 합을 저장할 변수와 중복을 판정할 셋을 생성한다.
2. 셋에 저장된 길이에 따라 중복을 판정하고, 조건에 맞게 출력한다.
"""

sum_angle = 0
angles = set()
for angle in range(3):
    angle = int(input())
    angles.add(angle)
    sum_angle += angle
# print(sum_angle, angles)

if sum_angle == 180:
    if  len(angles) == 1 and sum(list(angles)) == 60:
        print("Equilateral")
    if len(angles) == 2:
        print("Isosceles")
    if len(angles) == 3:
        print("Scalne")
# else:
    print("Error")
    

# a = int(input())
# b = int(input())
# c = int(input())

# if a + b + c == 180:
#     if a == 60 and b == 60 and c == 60:
#         print("Equilateral")
        
#     elif a == b or b == c or c == a:
#         print("Isosceles")
        
#     elif a != b and b !=c:
#         print("Scalene")
        
# else:
#     print("Error")
    
