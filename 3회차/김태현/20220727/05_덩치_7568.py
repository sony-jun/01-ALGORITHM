import sys
sys.stdin = open("05_덩치_7568.txt", "r")


N = int(input())
li = []

for i in range(N):
    li.append(input().split()) # [키, 몸무게] 리스트 생성 
                               # [['55', '185'], ['58', '183'], ['88', '186'], ['60', '175'], ['46', '155']]


for i in range(N): # k번째 덩치 [키, 몸무게]
    score = 1 # 일단 1등으로 설정
    for j in range(N): # k+1번째 덩치 [키, 몸무게]
        if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
            score += 1 # k번째 덩치를 1등 -> 2등으로 변경
    print(score, end=" ") # 더 크지 않으면, score = 1인 상태에서 출력
