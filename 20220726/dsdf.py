table = {1:{1:1200, 2:1350}, 2:{1:720, 2:800}, 3:{1:500, 2:500}}
age = 0
kind = 0
num = 0

while True:
    print('-' * 50)
    print('마을 버스 요금 계산기 입니다.')
    print('-' * 50)
    print()
    
    while True:
        age = int(input('''성인 : (1)    청소년 : (2)    어린이 : (3)
        >>>  '''))
        
        if age > 0 and age < 4:
            break
    
        else:
            print("잘못 선택하셨습니다. 다시 선택해주세요!!")
            continue   
    
    
    while True:
        kind = int(input('''교통카드 : (1)      현금 : (2)
        >>>  '''))
 
        if kind > 0 and kind < 3:
            break
        
        else:
            print("잘못 선택하셨습니다.다시 선택해주세요!!")
            continue
                        
    
    num = int(input("몇명인가요? >>> "))
    break
    
print()
print('총 요금은 ', table[age][kind] * num, '원 입니다') 