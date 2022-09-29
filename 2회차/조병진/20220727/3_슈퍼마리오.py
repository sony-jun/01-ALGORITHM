# 슈퍼 마리오
# 문제 : 10개가 일렬로 놓인 버섯의 점수를 먹으면서, 점수가 최대한 100에 가깝게 만들기

mushroom = []  # 10 20 30 40 50 60 70 80 90 100
for _ in range(10):
    mushroom.append(int(input()))

result = 0
score = 0
for i in mushroom:
    score += i
    if abs(score-100) <= abs(result-100):
        result = score

print(result)
