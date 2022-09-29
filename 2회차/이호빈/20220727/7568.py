n = int(input()) #브루트포스 문제

info = [] # 처음 정보 받을 리스트
ranking = [] # 등수정보를 저장할 리스트 ranking
for i in range(n):
    info.append(list(map(int, input().split())))
 
for i in range(n): # 0~4
    count = 0 # 등수 세기 위한 변수
    for j in range(n): #0~4
        if info[i][0] < info[j][0] and info[i][1] < info[j][1]: # 몸무게와 키 모두 자신보다 큰 사람의 수를 센다
            count += 1 
    ranking.append(count + 1) # 덩치 등수는 자신보다 몸무계 키 모두 큰 사람의 수 + 1 이므로 count + 1을 ans에 append한다.

for rank in ranking:
    print(rank,end=" ")


   