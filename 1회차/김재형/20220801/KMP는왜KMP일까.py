# 첫글자는 대문자
# 그 다음 소문자
# -뒤에는 대문자
# 대문자만 뺴고 전부 삭제

#Knuth-Morris-Pratt
word_ls = []
word = input()

for w in word:
    if ord(w) >= 65 and ord(w) <= 90:
        word_ls.append(w)

for i in word_ls:
    print(i,end='')