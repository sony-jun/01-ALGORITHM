n = int(input())

if n >=90 and n<=100:
    print('A')
elif n >=80 :
    print('B')
elif n >=70:
    print('C')
elif n >=60:
    print('D')
elif n<60 and n>=0:
    print('F')
else:
    print('점수의 범위는 0 ~ 100 입니다.')