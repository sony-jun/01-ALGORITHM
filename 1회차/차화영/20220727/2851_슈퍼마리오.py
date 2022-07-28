import sys
sys.stdin = open("2851.txt")

mushroom = [] # 버섯 점수 저장리스트
sum_ = 0 # 점수의 누적합을 0으로 초기화
for i in range(10):
    mushroom.append(int(input()))

for i in mushroom:
    sum_ += i
    if sum_ >= 100: # 누적합이 100보다 크거나 같을 때
        if abs(sum_ - 100) <= abs(100 -(sum_ -i)): # 직전의 누적합과 비교하여 100과의 차이가 더 작은 놈 출력
            break
        else:
            sum_ = sum_ -i # 그렇지 않으면 직전의 누적합 출력
            break
print(sum_)