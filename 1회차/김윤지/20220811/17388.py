# 리스트로 받기
skh = list(map(int,input().split()))

if sum(skh) >= 100: #합이 100이상 이면
    print('OK')

if sum(skh) < 100: #합이 100미만 이면 최솟값구해서 출력하기
    if min(skh) == skh[0]:
        print('Soongsil')
    elif min(skh) == skh[1]:
        print('Korea')
    else:
        print('Hanyang')