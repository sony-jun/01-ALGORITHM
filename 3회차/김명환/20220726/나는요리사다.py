score_list = [] # 각 요리사의 점수 입력받을 리스트 생성
for i in range(5):
    score_list.append(sum(map(int,input().split()))) # 점수 입력.
print(score_list.index(max(score_list))+1,max(score_list)) 

