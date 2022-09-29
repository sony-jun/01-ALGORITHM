while True: # 참일때까지 실행
    sentence = input()
    count = 0
    if sentence == '#': # 입력의 끝
        break # 문장 탈출
    for c in sentence:
        if c in 'aeiouAEIOU': # 모음이면
            count += 1 # count에 1씩 증가
    print(count)