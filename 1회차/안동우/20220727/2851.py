#마리오 최대 크기 100으로 근사치
#첫줄에 마리오 받는 점수 출력
# 만약 100이상 큰수 우선

# import sys
# sys.stdin = open("2851.txt", "r")

a = []
score = 0
for i in range(10):
    a.append(int(input()))    
for j in a:
    score += j #j 스코어 할당
    if score >= 100:#100이나 크면 print
        if score - 100 > 100 - (score - j):#100보다 작은수
            #142-100 100-(142-55)
            #42>13
            score -= j
            #142-55
        break
print(score)
#예시 87