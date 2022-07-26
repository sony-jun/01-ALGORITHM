result = {}

for i in range(5):
    score = list(map(int, input().split()))
    result[i] = sum(score)                          # 딕셔너리에 점수들의 합을 저장

# 딕셔너리를 값을 기준으로 정렬
result = sorted(result.items(), key=lambda x: x[1], reverse=True)

print(result[0][0] + 1, result[0][1])               # 딕셔너리의 첫 번째 키와 값을 출력
