import sys
sys.stdin = open("20220802/5063_TGN.txt")

N = int(input())

for test_case in range(N):
    r, e, c = map(int, input().split())     # r:광고X수익, e:광고O수익, c:광고비용

    if r < e - c:                   # 광고O이익(=광고O수익-광고비용) 높을 경우
        print('advertise')          # 광고를 해야 함
    elif r > e - c:                 # 광고X수익이 높을 경우
        print('do not advertise')   # 광고를 하지 않아야 함
    else:                           # 수익 차이가 없을 경우
        print('does not matter')    # 상관 없음