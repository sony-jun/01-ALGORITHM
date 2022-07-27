croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] # 크로아티아 알파벳을 변경한 것
word = input() # word 입력 받는다.

for i in croatia:
    word = word.replace(i, '!') # input 변수와 동일한 이름의 변수 # replace -> 문자열에서 어떠한 값을 찾아 변경해 주는 역할
                                # croatia 안에 있는 알파벳을 찾아서 ! 로 바꾼다.
print(len(word)) # word의 길이 출력