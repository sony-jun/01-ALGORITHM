Dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
        # 0      1      2      3      4       5      6       7

a = input() # 알파벳 입력
time = 0 # 걸리는 시간(변수를 0으로 초기화 -> 필요한 시간 파악하기 위해)

for i in range(len(a)):
    for j in Dial: # 이중 for문 사용 # Dial에 있는 문자열 하나하나 j로 반복
        if a[i] in j:
            # time += Dial.index(j) + 2 # WA -> 11 # UNUCIC -> 30
            time += Dial.index(j) + 3 # Dial의 index 수와 j가 0부터 반복하는 것을 감안해서 + 3

print(time)