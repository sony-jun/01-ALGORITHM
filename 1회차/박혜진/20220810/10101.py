triangle = []

for _ in range(3) :
    triangle.append(int(input()))

if sum(triangle) == 180 :

    if triangle[0] == triangle[1] == triangle[2] :
        print('Equilateral')

    elif triangle[0] == triangle[1] or triangle[0] == triangle[2] or triangle[1] == triangle[2] :
        print('Isosceles')
        
    else :
        print('Scalene')

else :
    print('Error')