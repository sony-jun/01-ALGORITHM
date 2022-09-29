# https://www.acmicpc.net/problem/1157

word = input().upper()              # 입력값 다 대문자로 바꾸기
word_2 = list(set(word))            # 입력값에서 중복값 없애기
l = []                              # 카운트 값 담을 리스트
for i in range(len(word_2)):        # 알파벳의 카운트 값을 담을 반복문
    l.append(word.count(word_2[i])) # 알파벳의 개수를 word에서 세고 리스트에 추가

if l.count(max(l)) > 1:             # 만약 최대값이 여러개면 ? 프린트
    print('?')
    
else:
    print(word_2[l.index(max(l))])  # 아니라면 최대값이 있는 인덱스 찾아서 해당 알파벳 프린트
    



            