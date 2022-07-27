# 크로아티아 리스트 만들기
# 문자열에서 크로아티아 비교한다 이때 우선순위(연속단어 알파벳 주의)

text = input()                                           # 문자 입력
cora = ['dz=', 'lj', 'nj', 'c=','c-', 'd-', 's=', 'z=']   # 크로아티아 알파벳 리스트_우선순위대로 정렬입력
i = 0
cnt = 0
while True:
    if len(text)>=3 and text[i:i+3] == 'dz=':
        cnt += 1
        if i+3 == len(text):
            break
        i += 3
    elif len(text)>=2 and text[i:i+2] in cora:
        cnt += 1
        if i+2 == len(text):
            break
        i += 2
    else:
        cnt += 1
        if i + 1 == len(text):
            break
        i += 1
print(cnt)