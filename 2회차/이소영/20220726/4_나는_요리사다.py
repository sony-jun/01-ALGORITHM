score = [] # 입력받은 수의 합계를 넣는 리스트

for i in range(5): # 5개줄
    score.append(sum(map(int, input().split()))) # 공백으로 구분된 점수를 int로 변환해서 합산 후 score에 넣기

print(score.index(max(score)) + 1, max(score)) # 우승자 번호, 점수
