# BAEKJOON1157
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
# 단, 대문자와 소문자를 구분하지 않는다.

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

print(ord('a'),ord('A'),ord('z'),ord('Z')) # a = 97 / A = 65 32차이,26개

word = input() 
word_ = []
for a in range(26): #알파벳 넣을 자리
    word_.append(0)
print(word_)

# word.upper() 를 사용하면 if문을 사용하지 않아도 됨
for c in word: #문자열을 가지고 문자별로 판단하여 word_에 카운트한다
    if ord(c) > 96: #문자가 소문자일경우
        word_[ord(c)-97] += 1
    elif ord(c) > 64: #문자가 대문자일 경우
        word_[ord(c)-65] += 1
print(word_)
count = 0 #최대값이 한개인가 확인하는 필터
where_1 = 0 #자릿수 카운트
for i in word_:
    where_1 += 1 # 1 = a
    if max(word_) == i :
        where_2 = where_1 #최대치와 같은수가 있는 자리
        count += 1
    elif count == 2:
        print('?')
        break
else:
    print(chr(where_2+64),where_2) #count2가 되지 않고 끝까지 돌아가면 이거 출력해줘