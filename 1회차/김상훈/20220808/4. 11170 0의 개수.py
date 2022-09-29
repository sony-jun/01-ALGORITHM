import sys
sys.stdin = open("4. 0의 개수.txt", "r")

# N부터 M까지의 수들을 종이에 적었을 때 종이에 적힌 0들을 세는 프로그램을 작성하라.

T = int(input()) # 테스트 케이스 갯수
for _ in range(T):
    N , M = map(int,input().split()) # 숫자의 범위 입력받기
    
    number_list = [] # 위 범위 내 숫자들 넣을 리스트
    
    cnt = 0 # 0이 나올떄마다 +1 해줄 공간.
    
    for n in range(N , M+1):
        number_list.append(n) #범위 내 숫자를 리스트에 모두 저장
    word_number = str(number_list) # 리스트 내 숫자들 문자열로 변환
    
    for i in word_number:
        if '0' in i: # 순회하다가 '0' 이 있으면
            cnt += 1 # cnt += 1
    print(cnt)
