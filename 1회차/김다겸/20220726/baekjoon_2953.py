score = []

# 5회 순회
for i in range(5):
    # input한 문자들을 숫자로 바꾼 후 그 값들을 모두 더한 후 score 리스트에 추가
    score.append(sum(map(int, input().split())))

# score의 최댓값을 가진 index와 score의 최댓값 출력
print(score.index(max(score))+1, max(score))