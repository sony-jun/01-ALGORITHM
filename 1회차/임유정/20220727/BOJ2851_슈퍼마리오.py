words = input() # word : mississipi
special_words = list(set(words)) # special_words = ['m','i','s','p'] # list 선언한 문자열 중 set함수를 이용해 중복제거
cnt_list = [] 

for i in special_words : # i = m, i, s, p
    cnt = words.count(i)
    cnt_list.append(cnt) # cnt 숫자를 리스트에 append함 # cnt_list=[4, 4, 1, 1]

if cnt_list.count(max(cnt_list)) > 1 : #count 숫자 최대값 중복시
    print("?")
else :
    print(special_list[(cnt_list.index(max(cnt_list)))].upper()) # count 숫자 최대값 위치 추출