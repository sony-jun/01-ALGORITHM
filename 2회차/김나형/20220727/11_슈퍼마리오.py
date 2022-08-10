import sys

sys.stdin = open("11_슈퍼마리오.txt")


mario_1 = 0
mario_2 = 0

for i in range(10): # 10번 반복하여 버섯 점수를 입력한다.
    mario_1 += int(input())
    if 100 - mario_2 >= abs(100-mario_1): # 100에 가장 가까운 값(100에서 뺏을 때 가장 적은 값)을 mario_2에 저장한다.
        mario_2 = mario_1 #  비교할 변수값(mario_2)을 가장 작은 값으로 저장한다.
print(mario_2)


        

    
    


