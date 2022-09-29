while True:
    #대문자 소문자를 다 소문자로 만들어준다.
    k = input().lower()
    result = 0
    #마지막 입력값인 '#'을 만나면 종료 
    if k == "#":
        break
    
    #문자열 한 개씩 돌면서 모음과 일치하면 += 1
    for i in k:
        if i in ['a', 'e', 'i', 'o', 'u']:
            result += 1

    print(result)


