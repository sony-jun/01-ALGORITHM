#백준 모음의 개수 1264
#영문 문장을 입력받아 모음의 개수를 세는 프로그램을 작성하시오. 모음은 'a', 'e', 'i', 'o', 'u'이며 대문자 또는 소문자이다.
Mo = {'A' ,'E' ,'I' ,'O' ,'U' ,'a' ,'e' ,'i' ,'o' ,'u'}
while True:
    T = list(map(str, input()))
    if '#' in T:
        break 
    count = 0
    for i in T:
        if i in Mo:
            count += 1
    print(count)