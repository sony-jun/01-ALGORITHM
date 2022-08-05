
test=int(input())
for i in range(test):
    r, e, c =  map(int, input().split()) 
    if e - r > c: #(광고했을때 수익)-(광고 안 했을때 수익)이 (광고비용)보다 크면 광고한다 
        print('advertise')
    elif e - r == c:
        print('does not matter')
    else:
        print('do not advertise')
