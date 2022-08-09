# 모음의 개수 세기

mo = ["a", "e", "i", "o", "u"]


while True: # "#"나오면 멈춰야 하기 때문에 while 사용(범위 순회가 아님)
    sentence = input().lower() # 소문자로 입력 받음

    if sentence == '#': # 문장에 #가 있으면 멈춤
        break

    cnt = 0 # 값 초기화 
    for i in sentence: # 입력 값 순회 
        if i in mo: # 철자 하나하나가 모음에 해당하는지 체크 
            cnt += 1 # 해당하면 1 추가
    
    print(cnt)
