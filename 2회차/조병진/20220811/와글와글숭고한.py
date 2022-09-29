# 와글와글 숭고한 🐳
# 문제 : 세 곳의 대학교의 참여도의 합을 구하고 필요하다면 압박하기

S, K, H = map(int, input().split())

TOTAL = S + K + H
LAST = min(S, K, H)

if TOTAL >= 100:
    print('OK')
else:
    if LAST == S:
        print('Soongsil')
    elif LAST == K:
        print('Korea')
    elif LAST == H:
        print('Hanyang')
