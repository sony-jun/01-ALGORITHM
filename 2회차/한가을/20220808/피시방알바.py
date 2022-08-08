# 1453
# 피시방에는 1번부터 100번까지 컴퓨터가 있다
# 손님은 모두 자기가 앉고 싶은 자리에만 앉고 싶어한다
# 들어오면서 번호를 말하고 만약 그 자리에 사람이 없으면
# 손님은 그 자리에 앉아서 컴퓨터를 할 수 있고 사람이 있다면 거절 당함
# 거절 당하는 사람의 수를 출력
# 자리는 맨 처음 모두 비어있고 자리에 앉으면 자리를 비우는 일은 없다

# 첫째 줄에 손님의 수 N이 주어진다
# 둘째 줄에 손님이 들어오는 순서대로
# 각 손님이 앉고 싶어하는 자리가 입력으로 주어진다

import sys
sys.stdin = open('피시방알바.txt')

N = int(input())
seats = list(map(int, input().split()))
#* set으로 중복값을 없애고 리스트에 넣고 길이를 셈
p = len(list(set(seats)))
#* 전체 손님 수에서 앉은 사람 수를 빼면 거절 당한 사람의 수가 나옴
print(N - p)