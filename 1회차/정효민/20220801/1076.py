a  = input()
b  = input()
c  = input()
color = ['black' , 'brown' , 'red' , 'orange' , 'yellow' , 'green' , 'blue' , 'violet' , 'grey' , 'white']

#값은 인덱스를 이용해서 위치를 찾는 식으로 찾으면 되고,곱은 10의 인덱스 제곱으로 하면 될지도
x = color.index(a)
y = color.index(b)
z = color.index(c)
print(z)
print(int(str(x) + str(y)) * (10 ** z))
