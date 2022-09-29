mushroom_list = []
score = 0
mario = 0

for i in range(10):
    mushroom_list.append(int(input())) # 버섯을 순서대로 먹고 계산

for mushroom in mushroom_list:
    mario += mushroom
    if abs(mario - 100) <= abs(score - 100): # 버섯을 먹은 다음 100을 뺀 다음 절댓값으로 변환해서 비교(가까운 값 찾기)
    # if abs(mario - 100) < abs(score - 100): # 100에 가까운 숫자가 2개일 경우 큰 값을 선택(X)
        score = mario
print(score)