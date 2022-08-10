W = []
K = []

for i in range(0, 10): # K 대학 참가한 10명의 점수
    W.append(int(input()))

for i in range(0, 10): # K 대학 참가한 10명의 점수
    K.append(int(input()))

W.sort(reverse=True) # W를 내림차순으로 정리
K.sort(reverse=True) # K를 내림차순으로 정리
wsum = 0
ksum = 0

for i in range(0, 3): # 각 학교별 인덱스 0,1,2에 있는 값을 더해줌
    wsum += W[i]
    ksum += K[i]
    
print(wsum, ksum)