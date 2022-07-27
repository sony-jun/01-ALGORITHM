# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
# 단, 대문자와 소문자를 구분하지 않는다.
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. => how to? 대문자사용 upper
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다. => how to? for/max/ifelse 

words = input().lower() # word : mississipi
special_words = list(set(words)) # special_words = ['m','i','s','p'] # list 선언한 문자열 중 set함수를 이용해 중복제거
cnt_list = [] 

for i in special_words : # i = m, i, s, p
    cnt = words.count(i)
    cnt_list.append(cnt) # cnt 숫자를 리스트에 append함 # cnt_list=[4, 4, 1, 1]

if cnt_list.count(max(cnt_list)) > 1 : #count 숫자 최대값 중복시
    print("?")
else :
    print(special_words[(cnt_list.index(max(cnt_list)))].upper()) # count 숫자 최대값 위치 추출 # special_list에서 문자열 추출

     


