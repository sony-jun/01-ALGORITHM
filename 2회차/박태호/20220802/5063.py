# TGN
# r = 광고 안하고 수익 100   -100    0
# e = 광고 하면 수익   130    -70  100
# c = 광고비용          30     40   70
# 광고 안하고 수익 ...
# 광고 하나 마나면 r+c == e 
# 광고 하면 손해 : 광고비용+ 수익이 광고 안하고 수익보다 낮다
case = int(input())

for _ in range(case):
    r,e,c = list(map(int, input().split()))
    if r+c == e:
        print('does not matter')
    elif e-c < r:
        print('do not advertise')
    else:
        print('advertise')
        