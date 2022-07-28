# https://www.acmicpc.net/problem/1292

import sys
sys.stdin = open("1292_input.txt")

# 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 6 6 6 6 6 6 ... 의 수열을 상상하자

# 위 수열의 A, B구간이 주어짐
A, B = map(int, input().split())

data = []

for i in range(B+1):      # B까지 순회하는 반복문
    for j in range(i):      # append 작업을 어디서 멈출지 정하기 위해 작성한 이중반복문
        if B == len(data):
            break
        data.append(i)    # 처음부터 B구간까지에 해당하는 모든 요소를 data 에 붙여줌

print(sum(data[A-1:B]))   # 처음부터 A-1구간까지에 해당하는 요소들은 data 에서 제외하려고
                          # 인덱싱 처리를 하고, 남아있는 data 의 요소들을 sum