x= int(input())
y= int(input()) # 각각 x, y 로 변수 선언하였으며. 인트 함수를 이용하여 숫자로 변환

if x > 0 and y > 0 :	# x,y: 양수
    print('1')
elif x < 0 and y > 0 :	# x:음수, y:양수
    print('2')
elif x < 0 and y < 0 :	# x,y: 음수
    print('3')
else:
    print('4')