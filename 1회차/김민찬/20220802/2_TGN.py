import sys

sys.stdin = open("2_TGN.txt")

N = int(input())
for i in range(N):
    r, e, c = map(int, input().split()) # r = 광고 하지 않았을 때 수익
    a = e - c # 광고 순수익(a) = 광고했을 때 수익(e) - 광고 비용(c)
    
    if r > a: # 광고 X 수익 > 광고 순수익
        print('do not advertise')
    elif r < a: # 광고 X 수익 < 광고 순수익
        print('advertise')
    else: # 그 외에는 'does not matter' (광고 X 수악 = 광고 순수익)
        print('does not matter')