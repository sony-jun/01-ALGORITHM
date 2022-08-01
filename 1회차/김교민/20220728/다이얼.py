alpha = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0
dial = input()

for i in range(len(dial)): #입력받은 단어 알파벳 하나하나 루프시킴
    for j in alpha:
        if dial[i] in j: # 입력 받은 문자가 j안에 있는 경우
            time += (alpha.index(j) + 3) #index는 0부터 시작해서 3을 더한다. 
print(time)