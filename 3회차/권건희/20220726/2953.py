#각점수는 타인의 평가의 합
# 들어오는게 총 5번이니까 반복문 써주기
#우승자와 점수를 같이 말해야함
# 우승자를 나타내는게 순서 밖에 없으니 리스트 채택
score=[]
for i in range(5):
    cgj=list(map(int,(input().split())))
    score.append(sum(cgj))
b_score=max(score)
print(score.index(b_score)+1,b_score)    