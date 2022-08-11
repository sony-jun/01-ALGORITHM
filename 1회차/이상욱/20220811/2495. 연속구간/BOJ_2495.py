import sys
sys.stdin = open ('2495.txt')

for i in range(3):
    max_num = 1                         # 같은 숫자가 가장 많은거 저장
    cnt = 1                             # 같은 숫자가 몇개인지 카운트하는 변수
    number = input()                    
    for j in range(1, len(number)):

        if number[j] == number[j-1]:    # 연속으로 동일한 숫자가 오면
            cnt += 1                    # 카운트 += 1
            if cnt > max_num:           # cnt가 max보다 크면
                max_num = cnt           # 그 숫자가 연속으로 가장 많이 나온숫자
        else:                           # 숫자가 연속으로 안나오면
            cnt =1                      # 카운트 = 1  
    print(max_num)
