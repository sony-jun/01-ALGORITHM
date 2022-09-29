N = int(input()) # 사람의 수 
weight_heigth = [] # 몸무게와 키 리스트 
rank_list = [] # 각각의 개인 등수
# 각각의 몸무게와 키를 입력받아 리스트로 묶은 뒤 몸무게와 키 리스트에 저장.
for i in range(N):
    w, h = map(int,input().split()) 
    weight_heigth.append([w, h])
# 반복문을 통해 키와 몸무게 각각 비교. 키와 몸무게가 나(i) 보다 비교대상(j)중에서 둘다 큰 사람이 있다면 count 
for i in range(N):
    cnt = 0
    for j in range(N):
        if weight_heigth[i][0]<weight_heigth[j][0] and weight_heigth[i][1]<weight_heigth[j][1]:
            cnt+=1
    rank_list.append(cnt+1) #등수는 N+1이라는 조건에 따라 1등부터 출력
#출력.
for i in range(N):
    print(rank_list[i],end=' ')
