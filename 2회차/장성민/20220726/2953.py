# 참가자들의 점수합을 위한 리스트 생성
total = []

# 각 점수들의 합을 total 리스트에 할당
for i in range(5):
    total.append(sum(map(int, input().split())))

# 우승자의 인덱스에 1 더한 값, 우승자의 점수 출력
print(total.index(max(total)) + 1, max(total))