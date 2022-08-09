# 백준 1264

# 영문 문장을 입력받아 모음의 개수를 세는 프로그램을 작성하시오. 모음은 'a', 'e', 'i', 'o', 'u'이며 대문자 또는 소문자이다.

while True:                                         # 입력받은 값이 # 일 때 까지 while 문을 통해 반복
    str = input()                               
    if str == '#':
        break
    cnt = 0
    for i in str:
        if i in 'aeiouAEIOU':                       # 알파벳 대 소문자를 반복문으로 실행하고 문자가 존재할 경우 카운트에 +1을 증가
            cnt += 1
    print(cnt)

