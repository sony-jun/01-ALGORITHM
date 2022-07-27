n = int(input())

data = [] # 입력된 정보 저장 리스트
ans = [] # 등수정보 저장 리스트
for i in range(n):
    a, b = map(int, input().split())
    data.append((a, b)) # 키와 몸무게 추가

for i in range(n):
    count = 0
    for j in range(n):
        # 자신보다 몸무게와 키가 큰 사람 수 확인
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            count += 1
    ans.append(count + 1)

for d in ans:
    print(d,end=" ")