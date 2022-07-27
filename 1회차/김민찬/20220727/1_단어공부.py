word = str(input()) # 문자열
word = word.upper() # 대문자
word_list = list(set(word)) # 입력받은 문자열에서 중복값 제거하여 정렬(무작위)

count = []
for i in range(len(word_list)): # 반복문을 활용하여 입력값에서 word_list의 요소들이 각각 몇 개가 있는지 개수를 count에 추가
    count.append(list(word).count(word_list[i])) # 입력의 count를 count 리스트에 추가
Max = max(count)

if count.count(max(count)) > 1: # 가장 많이 사용된 알파벳이 여러 개 존재할 경우에는 '?' 출력
    print('?')
else:
    print(word_list[count.index(Max)]) # 최댓값이 하나면 숫자 리스트 중에서 가장 큰 수의 위치를 index로 찾아
                                       # index에 위치한 문자열을 출력