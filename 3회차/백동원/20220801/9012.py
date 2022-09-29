# 괄호 
                                        
T = int(input())                        
for _ in range(T):                      # 괄호로 구성된 문자열을 리스트로 변환하는 과정
    word = input()
    words_list = []
    word_cnt = 0
    for i in word:
        words_list.append(i)            
    while len(words_list) > 0:          # 리스트의 길이가 0이되면 멈추는 반복문
        pop_result = words_list.pop()   # 뒤에서 하나 뽑아 변수에 할당
        if pop_result == ')':           # 그 변수가 ) 이면 
            word_cnt += 1               # 카운트 1 추가
        else:                           # ( 이면 
            word_cnt -= 1               # 카운트 1 차감
        if word_cnt < 0:                # 카운트가 0보다 작은 순간이 생기면
            print('NO')                 # ( 가 ) 보다 더 많아졌다는 뜻이므로
            break                       # 괄호 문자열은 절대 올바를 수 없다. 바로 컷
    if word_cnt == 0:                   # 카운트가 0으로 맞아 떨어지면 
        print('YES')                    # 올바른 괄호 문자열이므로 yes
    elif word_cnt > 0:                  # 0보다 크면
        print('NO')                     # ) 가 ( 보다 많은 것이므로 no