# N권의 교과서는 각각 1부터 N까지의 번호가 매겨져 있다.
# 각 더미의 맨 위에 있는 교과서만 꺼낼 수 있으며
# 반드시 교과서를 꺼낸 순서대로 나열해야 하기 때문에
# 번호순으로 나열하기 위해서는 1번, 2번, ... N - 1번, N번
# 교과서 순으로 꺼내야 한다.

# 첫째 줄에 교과서의 수 N, 교과서 더미의 수 M이 주어진다
# 둘째 줄부터 2 * M 줄에 걸쳐 각 더미의 정보가 주어진다
# i 번째 더미를 나타내는 첫 번째 줄에는
# 더미에 쌓인 교과서의 수 ki가 주어지며
# 두 번째 줄에는 ki 개의 정수가 공백으로 구분되어 주어진다
# 각 정수는 교과서의 번호를 나타내며
# 아래에 있는 교과서의 번호부터 주어진다
# 교과서의 번호는 1부터 N까지의 정수가 한 번씩만 등장

# 올바른 순서대로 교과서를 꺼낼 수 있다면 yes
# 불가능하다면 no를 출력

import sys

# input = sys.stdin.readline
sys.stdin = open('자료구조는정말최고야.txt', 'r')

n, m = map(int, input().split())
p = True

for _ in range(m):
    i = int(input())
    input_list = list(map(int, input().split()))
    if input_list != sorted(input_list, reverse=True):
        p = False
        break

if p:
    print('Yes')
else:
    print('No')

# 더미는 중복되지 않으며 책이 1권씩 있기 때문에
# 한 개의 더미라도 내림차순이 아니라면 올바르게 나열할 수 없다