# 0~999999 
import sys

sys.stdin = open("암호문.txt", "r")



for test_case in range(1,10+1):
    
    length_pass = int(input())
    password = list(map(int, input().split()))
    num_order = int(input())
    order = list(input().split())

 
    for i in range(len(order)):
        if order[i] == 'I':
            position = int(order[i+1])
            numbers = int(order[i+2])
            for j in range(numbers):
                password.insert(position+j, int(order[i+2+j+1]))
    
    answer = ' '.join(map(str,password[:10]))
    print(f'#{test_case} {answer}')

    '''
    처음에 I를 찾고 나서 명령문에 따라 x번째 자리에 y개의 암호를 넣는 부분에서
    아이디어가 떠오른것이 y개만큼 슬라이싱 하여 insert 해보고자 하였는데 계속 고집하다가 마지막까지 
    아무 반응이 없어서 쩔쩔맸습니다..(아마 제대로 모르고 쓴것 같습니다)
    insert를 하니 한번에 여러개를 넣을 수는 없는 것을 알아서 슬라이싱 한것을 통째로 넣는것은 포기하고
    하나씩 넣는 것으로 생각을 다시 하여 해결하였습니다.  
    
    '''