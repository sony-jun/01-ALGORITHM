sequence = 0 # 최댓값 순서
max = 0 # 최댓값

for i in range(5):
    A = list(map(int, input().split()))

    if sum(A) > max: # 최댓값 비교
        max = sum(A)
        sequence = i + 1
print(sequence, max)
# 리스트 입력을 받으면서 리스트의 최댓값을 비교하여
# sequence를 저장한 후에, sequence와 max를 출력