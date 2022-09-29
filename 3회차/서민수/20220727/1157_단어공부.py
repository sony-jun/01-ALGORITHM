# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

# 예제 입력 1 
# Mississipi
# 예제 출력 1 
# ?
# 예제 입력 2 
# zZa
# 예제 출력 2 
# Z
# 예제 입력 3 
# z
# 예제 출력 3 
# Z
# 예제 입력 4 
# baaa
# 예제 출력 4 
# A

word = input().upper() # 입력을 대문자로 받는다.
set_word = list(set((word))) # 입력받은 문자열에서 중복값을 제거
lst = [] # 반복횟수를 담기 위한 리스트 초기화

for i in set_word: # 입력받은 문자 열에서 중복을 제거한 각각의 문자들을 사용
    # print(i) # zZi 입력 zZi 출력
    cnt = word.count(i) # 해당 단어들이 개수가 몇개있는지 체크
    # print(cnt) # zZi 입력 i1 z1 Z1 출력
    lst.append(cnt) ## 개수를 리스트에 append
    # print(lst)  # zZi 입력 [1,1,1] 출력
if lst.count(max(lst))  > 1: # lst의 개수 최대값이 중복되면
    # print(lst)
    print('?') # ?를 출력
 
else: # 그렇지 않을 경우
    count = lst.index(max(lst)) # count 숫자(개수의) 최대값 인덱스(위치) 를 찾는다.
   #  print(count)
    print(set_word[count]) # 해당 인덱스에 있는 단어 출력