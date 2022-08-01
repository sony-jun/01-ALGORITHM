# 백준 7568
# 사람의 덩치를 키와 몸무게, 두 개의 값으로 표현하여 등수를 매김
# 어떤 사람의 몸무게가 x kg이고 키가 y cm라면
# 이 사람의 덩치는 (x, y) 로 표시

# 첫 줄에는 전체 사람의 수가 주어짐
# 이어지는 N개의 줄에는 각 사람의 몸무게와 키를 나타내는
# 양의 정수 x와 y가 하나의 공백을 두고 각각 나타남

# 입력에 나열된 사람의 덩치 등수를 구해
# 그 순서대로 첫 줄에 출력
# 단, 각 덩치 등수는 공백 문자로 분리되어야 함


n = int(input())
data = []

for i in range(n):
    data.append(input().split())
data_len = len(data)
seq = []

for i in range(data_len):
    count = 1
    for j in range(data_len):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            count += 1
    seq.append(count)

for i in seq:
    print(i, end = ' ')