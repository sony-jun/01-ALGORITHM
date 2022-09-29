# https://www.acmicpc.net/problem/17388

scores = list(map(int, input().split()))

if sum(scores) >= 100:
    print('OK')
else:
    if min(scores) == scores[0]:
        print('Soongsil')
    elif min(scores) == scores[1]:
        print('Korea')
    else:
        print('Hanyang')