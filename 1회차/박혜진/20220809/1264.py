# 모음의 개수를 세는 딕셔너리
aeiou = {'A' : 0,
         'E' : 0,
         'I' : 0,
         'O' : 0,
         'U' : 0   
}

# 대문자로 입력받기
while True :
    word = input().upper()
    # '#'을 입력받으면 반복문 그만하기
    if word == '#' :
        break

    else :
        # 각 모음의 개수 세기
        for i in word :
            for o in aeiou :
                if i == o :
                    aeiou[o] = word.count(i)

        # 모음의 개수의 합
        sum = 0
        for j in aeiou :
            sum += aeiou[j]
        print(sum)

# 정답 코드

while True :
    w = input()

    if w == '#' :
        break

    else :
        cnt = 0
        for i in w :
            # 대문자 소문자 각각 쓰기
            if i in 'aeiouAEIOU' :
                cnt += 1
        print(cnt)