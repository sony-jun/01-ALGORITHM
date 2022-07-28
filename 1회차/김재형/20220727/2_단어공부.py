# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

# 대문자 소문자 구분 x => upper로 통일
word = input()
word = word.upper()
#print(word)

# 딕셔너리 활용 / 가장 많이 사용한 알파벳과 횟수
word_dict = {}
# 가장 많이 사용한 알파벳이 몇갠지 확인할 때 사용
a = []

# 딕셔너리에 키값 부여
for i in word:
    word_dict[i] = 0
    
# 알파벳 갯수
for j in word:
    word_dict[j] += 1
# print(word_dict)

# 가장 많은 사용된 횟수
most = max(word_dict.values())

for key, value in word_dict.items():
    if value == most:   # 가장 많이 사용한 알파벳의 횟수와 비교해서 같으면
        a.append(key)   # 리스트 a에 추가
if len(a) >= 2:  # 추가한 리스트의 길이가 2이상이면 가장 많이 사용한 알파벳이 2개 이상이란 소리니까
    print('?')
if len(a) == 1: # 길이가 1이면
    print(a[0]) # 리스트의 인덱스 0의 값을 출력
    
#============================================================

# word = input().upper() #출력은 대문자가 나와야 하기때문에 처음부터 대문자로 변환
# word_li = list(set(word)) #문자열 각각의 개수를 구해야하기에 list로 변환

# cnt_li = [word.count(i) for i in word_li]
# # word_li에 있는 i가 word에 몇개 있는지 카운트해서 cnt_li를 만들어줘  
# # print(cnt_li)[4, 4, 1, 1]
# if cnt_li.count(max(cnt_li)) > 1: #만약 cnt_li에 max값을 카운트했는데 1보다 많으면
#     print('?')    # ? 출력

# else:
#     max_index = cnt_li.index(max(cnt_li))  #cnt_li에서 가장 많이 있는 인덱스위치를 반환
#     print(word_li[max_index])  #word_li에서 가장 많은 알파벳 출력