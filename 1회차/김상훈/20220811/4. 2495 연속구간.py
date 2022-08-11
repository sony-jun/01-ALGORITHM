import sys
sys.stdin = open("4. 연속구간.txt", "r")


for _ in range(3):
    number = input() # 입력 3개
    
     # 연속된 수가 아예 없을 때 1이므로 두 변수는 1로 시작.
     
    max = 1 # 연속 증가 수가 여러 개일 경우 최대값을 갱신받기 위한 변수

    count = 1 # 연속 숫자가 나올경우 1씩 증가하는 변수 (max에 최댓값 전달할 변수.)
    
    
    for i in range(1,8): # 자릿수 8개이므로 1~8까지 반복.
                         # 범위를 0~7로 하면 맨 앞의'1'을 비교할 대상이 없음
                         
        if number[i] == number[i-1]: # number의 i번쨰 요소와 그 이전 요소가 같으면
            count += 1 # count 1 증가
            
            if count > max: # count가 max보다 커지면
                max = count # max에 count 값 저장
        else : # i와 i-1 요소가 다르면 
            count = 1 # count 1로 변경 후 반복 진행

    print(max)
    

