# 나는 요리사다
# 5명의 참가자
# 점수는 1~5
# 각 참가자가 얻은 점수는 다른사람이 평가해 준 점수의 합.
# 우승자를 가려내라.
# 입력값 = 각 참가자가 얻은 네개의 평가 점수, 네개의 입력값을 띄어쓰기로 받는다.
# 조건 : 우승자는 유일하다.
# 출력 : 우승자의 번호와 그가 얻은 점수.
chef_score = {}
for chef_num in range(1,6):
    score = map(int, input().split())
    chef_score[chef_num]=sum(score)

maxkey = max(chef_score,key=chef_score.get)
maxvalue = max(chef_score.values())
# print(chef_score)
print(maxkey, maxvalue, sep = ' ')
