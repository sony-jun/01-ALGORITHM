S, K, H = list(map(int, input().split()))
all = [S, K, H]
if sum(all) >= 100:
    print('OK')
else:
    if min(all) == S:
        print('Soongsil')
    elif min(all) == K:
        print('Korea')
    else:
        print('Hanyang')