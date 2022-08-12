
# '#'이 끝나면 멈춘다
while True:
    word = input()
    if word == '#':
        break
    # 모음을 리스트로 입력
    alphabet = ['a','e', 'i','o','u', 'A', 'E', 'I', 'O', 'U']
    result = 0 
    # 입력한 문자열의 길이를 반복문으로
    for i in range(len(word)):
        # word에 있는 문자열이 alphabet에 있으면
        if word[i] in alphabet:
            # 1씩증가
            result += 1
    print(result)
