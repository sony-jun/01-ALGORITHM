word = input()
word_list = []

for i in word:
    if ord(i) <= 90:                        # 대문자이면
        word_list.append(chr(ord(i) + 32))  # 소문자로 바꿔 리스트에 저장
    else:                                   # 소문자이면
        word_list.append(i)                 # 그대로 저장

dif_word_list = list(set(word_list))        # 중복제거 후 리스트로 형변환
count_list = []
for j in dif_word_list:                     # 중복제거한 리스트에서 하나씩 꺼내
    cnt = 0
    for h in word_list:                     # 원래 단어와 비교하면서
        if j == h:                          # 카운트한다.
            cnt += 1
    count_list.append(cnt)                  # 카운트가 종료되면 새로운 리스트에 카운트 결과 저장
if count_list.count(max(count_list)) >= 2:  # 만약 최대값이 2개 이상 발견되면
    print('?')                              # ? 출력
else:                                                                      # 그게 아니라면
    print(chr(ord(dif_word_list[count_list.index(max(count_list))]) - 32)) # 최댓값의 인덱스를 찾아 그 철자를 찾고 대문자로 변경하여 출력