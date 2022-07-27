# 문자열 대문자 변경, 중복 제거
word = input().upper()
word_list = list(set(word))

# 각 알파벳 숫자를 리스트에 할당
cnt = []
for i in word_list:
    cnt.append(word.count(i))

# 숫자 최대값이 여러 개이면 if, 1개면 else
if cnt.count(max(cnt)) > 1:
    print("?")
else:
    max_ = cnt.index(max(cnt))
    print(word_list[max_])