# FBI 🐳
# 문제 : FBI명이 들어간 첩보원 찾기

SPY = [input().strip() for _ in range(5)]

FBI = False  # 초기값 0
for i in range(len(SPY)):
    if 'FBI' in SPY[i]:  # 해당 인덱스 문자열에 'FBI' 가 포함되면
        print(i + 1, end=' ')
        FBI = True

if not FBI:
    print('HE GOT AWAY!')
