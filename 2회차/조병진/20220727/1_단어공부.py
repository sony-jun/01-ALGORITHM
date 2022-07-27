# 단어공부
# 문제 : 대소문자로 구성된 단어에서 가장 많이 사용된 알파벳 구하기
#       가장 많이 사용된 알파벳이 여러 개라면 '?' 출력

word = input().upper()  # MISSISSIPI
word_list = list(set(word))  # S I P M

result = []

for i in word_list:
    cnt = word.count(i)  # 4411
    result.append(cnt)

max_ = max(result)
if result.count(max_) >= 2:
    print('?')
else:
    print(word_list[result.index(max_)])
