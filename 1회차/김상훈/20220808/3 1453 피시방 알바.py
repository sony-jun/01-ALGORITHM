import sys
sys.stdin = open("3. 피시방 알바.txt", "r")


N = int(input()) #입장하는 손님 수
jali = list(map(int,input().split())) # 손님이 앉고싶은 자리번호

seat = len(list(set(jali))) # 자리 리스트의 중복을 제거한 길이를 seat 리스트에 저장
print(N-seat) # 손님 수에서 중복 제거한 값을 빼면 중복 횟수가 나옴.
    
    