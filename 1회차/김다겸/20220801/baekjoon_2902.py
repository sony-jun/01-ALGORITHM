name = input()

for i in name:
    # name의 문자 하나씩 아스키코드로 바꿈
    ascii = ord(i)
    # 만약 문자가 대문자라면
    if ascii >= 65 and ascii <= 90:
        # 그 문자 출력
        print(i, end='')