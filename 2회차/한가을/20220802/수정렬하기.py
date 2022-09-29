# 백준 2750
# N개의 수가 주어졌을 때
# 이를 오름차순으로 정렬

# 첫째 줄에 수의 개수 N이 주어진다
# 둘째 줄부터 N개의 줄에는 수 주어진다
# 수는 중복 되지 않는다

# 첫째 줄부터 N개의 줄에
# 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력

import sys
sys.stdin = open('수정렬하기.txt', 'r')

# 주어질 수의 개수
N = int(input())
# 숫자를 담을 리스트
num_list = []

for i in range(N):
    # 받은 숫자를 num_list에 추가
    num_list.append(int(input()))
# 받은 숫자를 정렬
num_list = sorted(num_list)

# 요소들을 하나씩 출력
for i in range(len(num_list)):
    print(num_list[i])