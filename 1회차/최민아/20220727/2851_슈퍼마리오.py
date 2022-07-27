import sys
sys.stdin = open("20220727/2851_슈퍼마리오.txt")

score = 0                           # 점수 초기값은 0
mushroom = []                       # 각 버섯의 점수를 저장할 리스트

for i in range(10):                 # 10개의 버섯
    mushroom.append(int(input()))   # 각 버섯 점수 입력

for point in mushroom:
    score += point                  # 순서대로 버섯 먹어서 점수 얻기
    if score > 100:                 # 점수가 100을 넘으면
        if score - 100 > 100 - (score - point): # 현재와 직전 점수 비교
            score = score - point   # 100에 더 가까운 점수가 최종 점수
        break

print(score)                        # 최종 점수 출력