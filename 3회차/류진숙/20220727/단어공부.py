# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

# 우선, 문자열에서 알파벳 소문자 대문자 같은걸로 인식하는지 확인해본다.

# word = 'zZa'

# cnt = 0
# for str in word:
#     if str == 'z':
#         cnt += 1

# print(cnt)

# 같은 걸로 인식 안함 - 다른 방법 고안
# 우선 전부 다 대문자로 바꾼다음에 대문자 겹치는 문자를 튀어 나오게 하자!


word = input()
word = word.upper() # 대문자로 바꿔 준다

str_dict = {}
for str in word:
    if str not in str_dict:
        str_dict[str] = 1
    else:
        str_dict[str] += 1

v_list = list(str_dict.values())
v_list = list(map(int, v_list))

final_list = []
for key, value in str_dict.items():
    if value == max(v_list):
        final_list.append(key)

if len(final_list) > 1:
    print('?')
elif len(final_list) == 1:
    print(final_list[0])

# 정답 264 ms

# 구글링 검색     
word = input().upper()
word_list = list(set(word))
cnt = []

for i in word_list:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(word_list[(cnt.index(max(cnt)))])

# 정답 108 ms

