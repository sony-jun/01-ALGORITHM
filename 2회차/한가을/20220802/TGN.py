# 백준 5063
# 첫째 줄에 테스트 케이스의 개수 N이 주어진다
# 다음 N개의 줄에는 3개의 정수 r, e, c 가 주어진다
# r은 광고를 하지 않았을 때의 수익
# e는 광고를 했을 때의 수익
# c는 광고 비용

# 광고를 해야하면 advertise
# 하지 않아야 하면 do not advertise
# 광고를 해도 수익이 차이가 없다면 does not matter

import sys
sys.stdin = open('TGN.txt', 'r')

T = int(input())

for i in range(T):
    r, e, c = map(int, input().split())
    # 광고 하지 않은 수익이 (광고 수익 - 광고 비용) 보다 작으면
    if r < (e - c):
        print('advertise')
    # 광고 하지 않은 수익이 (광고 수익 - 광고 비용) 보다 크면
    elif r > (e - c):
        print('do not advertise')
    # 광고 하지 않은 수익과 (광고 수익 - 광고 비용)이 같으면
    elif r == (e - c):
        print('does not matter')