import sys
sys.stdin = open("4. 소가 길을 건너간 이유 1.txt", "r")


N = int(input())
cow = [None] * 11
# 소는 10마리 (1마리 시작이므로 1~11)
# 위치가 정해져있지 않으므로 None으로 설정

cnt = 0
# 소가 건너갈 최소 횟수

for _ in range(N):
# 관찰 횟수만큼 반복
    cow_number , move = map(int,input().split())
    # 소의 이전 위치와 이동여부를 저장하는 변수 생성
    
    if cow[cow_number] == None:
    # 소의 위치가 저장되어있지 않으면 
        cow[cow_number] = move
    # 소의 위치에 이동값을 저장.    
    else:
        if cow[cow_number] != move:
            # 저장한 소의 위치와 이동값이 다르면.
            
            cnt += 1
            # 이동한 횟수 +1 추가 후
            
            cow[cow_number] = move
            # 해당 소의 위치를 이동값으로 바꾼다.
print(cnt)
    
    

