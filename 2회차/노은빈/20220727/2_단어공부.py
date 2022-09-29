word = input().upper()   #대문자로 입력 받기
many = list(set(word))   #중복된 값들 지우기

cntlst = []   #빈 리스트 만들기

for i in many:
    cnt = word.count(i)  #입력받은 word 개수 세기
    cntlst.append(cnt)   #빈 리스트에 개수 추가

if cntlst.count(max(cntlst)) >= 2 :
    print('?')   #cnt 숫자 최대값이 중복되면
else :
    max_index = cntlst.index(max(cntlst))  # count 숫자 최대값 인덱스(=위치)
    print(many[max_index])   # count 숫자 최대값 인덱스 print