#백준 사분면 9610
#2차원 좌표 상의 여러 점의 좌표 (x,y)가 주어졌을 때, 각 사분면과 축에 점이 몇 개 있는지 구하는 프로그램을 작성하시오.
my_dic = {
    'Q1:': 0,
    'Q2:': 0,
    'Q3:': 0,
    'Q4:': 0,
    'AXIS:': 0
}
for TC in range(int(input())):
    X, Y = map(int, (input().split()))
    if X == 0 or Y == 0:
        my_dic['AXIS:'] += 1
    elif X > 0 and Y > 0:
        my_dic['Q1:'] += 1
    elif X < 0 and Y > 0:
        my_dic['Q2:'] += 1
    elif X < 0 and Y < 0:
        my_dic['Q3:'] += 1
    elif X > 0 and Y < 0:
        my_dic['Q4:'] += 1
answer = my_dic.items()
for key, value in answer:
    print(key,value)