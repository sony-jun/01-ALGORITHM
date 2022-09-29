n = int(input())
pi = list(map(int, input().split()))
temp = 0
result = []

h = []
for i in range(1, len(pi)):
    h.append(pi[i] - pi[i - 1])         # 높이의 차를 배열에 저장

for i in h:
    if i > 0:                           # 높이의 차가 양수면 오르막길
        temp += i                       # 오르막길의 높이를 누적
    else:
        result.append(temp)             # 내리막길을 만나면 직전 오르막길의 높이들을 배열에 저장
        temp = 0
else:
    result.append(temp)                 # 내리막길을 만나지 않아도 등산이 끝나면 오르막길 높이 저장

print(max(result))                      # 가장 큰 오르막길의 높이를 출력
