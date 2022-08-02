# TGN
# 문제 : 광고 효과가 주어졌을 때, 광고를 해야할지 말아야할지 결정하는 프로그램을 작성하시오.
# 출력 : 각 테스트 케이스에 대해서, 광고를 해야 하면 "advertise", 하지 않아야 하면 "do not advertise", 광고를 해도 수익이 차이가 없다면 "does not matter"를 출력한다.

n = int(input())

for i in range(n):
    r, e, c = map(int, input().split())

    margin = e - c
    if r < margin:
        print('advertise')
    elif r == margin:
        print('does not matter')
    else:
        print('do not advertise')
