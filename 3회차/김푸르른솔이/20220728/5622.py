alphabet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
time = 0

for i in word:
    for j in alphabet: #이중 반복문을 이용해서 ALPHA에 잇는 문자열을 반복하고
        if i in j: # 입력받은 알파벳이 j문자열에 당하면
            time += alphabet.index(j) + 3
print(time)
