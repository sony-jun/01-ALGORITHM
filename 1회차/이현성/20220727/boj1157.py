words = str(input())
str_list = []

for word in words:
    if word not in str_list:
        str_list.append(word)

str_list = ''.join(str_list)

cnt_list = []
for i in range(len(str_list)):
    cnt_ = words.count(str_list[i])
    cnt_list.append(cnt_)

max_area = cnt_list.index(max(cnt_list))

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    print(str_list[max_area].upper())







words = input() # input 값 문자열로 받기
str_list = [] # 문자열의 문자를 저장 할 list

for word in words: # word 가 input 받아온 문자열(words)에 있는지
    if word not in str_list: # if 만약 word가 문자열의 문자를 저장할 list(str_list)에 없다면
        str_list.append(word) # 문자를 저장할 list에 추가해라 문자(word)를
# print(str_list) # ['M', 'i', 's', 'p']

str_list = ''.join(str_list) # list str_list를 문자열로 변환
# print(str_list) # Misp

cnt_list = [] # 문자의 갯수를 저장할 빈 list 생성
for i in range(len(str_list)): # 문자의 길이 만큼 반복
    cnt_ = words.count(str_list[i]) # cnt_ 는 input 문자열에서 추린문자열Misp를 순서대로 센 값
    cnt_list.append(cnt_) # cnt_list에 추가한다 input문자열에서 각 문자 Misp의 갯수를
# print(cnt_) # [1, 4, 4, 1]

max_area = cnt_list.index(max(cnt_list)) # cnt_list에서 제일 큰 수가 있는 위치 값 을 max_area에 저장
# print(max_area) # 2 

if cnt_list.count(max(cnt_list)) > 1: # 만약 가장 큰 문자 갯수를 셋을 때 1보다 크다면
    print('?') # print '?'
else: # 그게 아니라면
    print(str_list[max_area].upper()) # print 갯수가 가장 많았던 위치에 있는 문자열을 대문자로 출력