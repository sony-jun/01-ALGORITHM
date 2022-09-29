import sys
sys.stdin = open('B10816.txt')

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))
#print(N, N_list, M, M_list)
cnt = {} # 엔 중복 먼저 거르고 그 다음 엠에 잇는거 바로 카운트
result = {}
for i in N_list:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1
# print(cnt) {6: 1, 3: 2, 2: 1, 10: 3, -10: 2, 7: 1}
for i in M_list:
    if i in cnt:
        print(cnt[i], end = ' ')
    else:
        print(0, end = ' ')