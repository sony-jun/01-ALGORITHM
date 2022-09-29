S = input().upper() #대소문자를 구분하지 않는다고 문제에 놔와있으므로 lower도 가능
list_ = list(set(S))
#set으로 중복을 배제해주간 하지만 순서가 없기 때문에 인덱스 함수가 불가능하다.
# 그래서 list로 한번 더 변환해준다.
cnt = [] #반복문으로 list내의 요소들의 개수를 넣기 위한 빈 리스트를 만들기

for i in list_:
    cnt.append(S.count(i))
# 아래 if문 들여쓰기 하면 안 된다.
if cnt.count(max(cnt)) > 1: # count한 숫자의 최대값이 중복일 경우
    print("?")
else:
    print(list_[cnt.index(max(cnt))])