# 나는요리사다
# "나는 요리사다"는 다섯 참가자들이 서로의 요리 실력을 뽐내는 티비 프로이다. 
# 각 참가자는 자신있는 음식을 하나씩 만들어오고, 서로 다른 사람의 음식을 점수로 평가해준다. 점수는 1점부터 5점까지 있다.
# 각 참가자가 얻은 점수는 다른 사람이 평가해 준 점수의 합이다. 이 쇼의 우승자는 가장 많은 점수를 얻은 사람이 된다.
# 각 참가자가 얻은 평가 점수가 주어졌을 때, 우승자와 그의 점수를 구하는 프로그램을 작성하시오.

# 초기모델
result = [] # 딕셔너리 생성
for i in range(5): # 5명이 본인 제외한 4명한테 평가 받음 -> 점수 입력
    score = map(int, input().split()) # 입력값은 공백으로 구분되어짐
    result.append(sum(score)) # 평가점수 합산은 순차적으로 result 딕셔너리에 추가
print(result.index(max(result)) + 1, max(result)) # 최고득점한 참가자의 번호(0부터 시작하니 +1), 최고득점 점수 출력

# 코드 간략화 버전(1차)
score = [] 
for i in range(5):
  score.append(sum(map(int, input().split()))) 
print(score.index(max(score))+1, max(score)) 

# 코드 간략화 버전(최종)
score = [sum(list(map(int,input().split()))) for i in range(5)]
print(score.index(max(score))+1,max(score))