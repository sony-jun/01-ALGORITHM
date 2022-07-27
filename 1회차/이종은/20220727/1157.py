n = input().upper() # 처음에 입력 받는 문자는 대소문자를 구분하지 않기 때문에 upper함수를 이용하여 문자열을 모두 대문자로 변환 

count_words = list(set(n)) #입력 받은 문자열 중 중복되는 요소는 set함수를 이용해 제거 => Z,A
#이 리스트는 입력 받은 문자에서 알파벳이 몇 번 사용되는지 확인 

list_ = [] # 알파벳이 몇 개 있는지 숫자를 세고 담아줌
for i in count_words : 
    # print(i) # Z,A
    cnt = n.count(i) # n 입력 값에서 중복 되어 제거 된 요소가 몇번사용 됬는지 센다. 
    # print(cnt) # 2, 1
    list_.append(cnt) # count 숫자를 리스트에 담아줌
    # print(list_) #[2,1]

if list_.count(max(list_)) > 1 : # 숫자 리스트에서 알파벳이 사용 된 개수 중 가장 큰 갯수(예를 들면 4)가 두개라면 
    print('?') # 물음표 출력
else : 
    max_index = list_.index(max(list_)) #1보다 큰 것이 아니라면 숫자 리스트에서 가장 큰 수의 위치를 인덱스로 찾음
    # 여기서 list_에서 2,1 이고 2는 인덱스가 0임
    print(count_words[max_index]) # count_words는 Z,A이므로 0은 Z
