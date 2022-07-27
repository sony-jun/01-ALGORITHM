# 단어공부

# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
# 입력: 첫째줄에 알파벳 대소문자로 이루어진 단어가 주어진다.
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.


# 1차 모델
word = input().upper() # 입력 후 대문자로 변경
word_list = list(set(word)) # 중복값 제거하여 word_list에 요소 삽입 

cnt = [] # 빈 리스트 생성
for i in word_list:
  cnt.append(word.count(i)) # 해당 요소가 몇개 있는지 체크

if cnt.count(max(cnt)) > 1: # 가장 많이 사용된 알파벳 개수가 여러개일때 ? 출력
  print("?")
else:  # cnt 딕셔너리에서 가장 큰 수의 위치(index)를 반환하고 그 수를 word_list로 보내 문자열을 출력
  print(word_list[(cnt.index(max(cnt)))])



# 코드 간소화(최종)
word = input().upper() 
word_list = list(set(word)) 

cnt = [word.count (i) for i in word_list]
print("?") if cnt.count(max(cnt)) > 1 else print(word_list[(cnt.index(max(cnt)))])

