# https://www.acmicpc.net/problem/5063

N = int(input())
# r : 광고를 하지않았을때의 수익, e: 광고를 했을때의 수익, c: 광고비용
for i in range(N):
    r, e, c = map(int, input().split()) 
    if r + c < e: # 광고를 했을때의 수익 보다, 하지않았을떄 + 광고비용이 클떄
        print('advertise')
    elif r + c > e: # 했을때의 수익이 클때
        print('do not advertise')
    else: # 차이가 없을떄
        print('does not matter')