# 어퍼 메소드를 사용하여 전체 문자를 대문자로 변환하여 변수에 저장한다.
# 비교를 하기위해 셋 함수를 사용하여 중복된 문자값을 제거한 후 변수에 저장한다
# 폴문을 이용하여 알파벳이 사용된 횟수를 리스트에 저장한다.
# 이프문을 사용하여 출력문을 작성하고, 알파벳이 사용된 갯주 중 1보다 크면 물음표를 출력하게 한다.
# 최대값이 하나라면 숫자 리스트 중에서 가장 큰 수의 위치를 인덱스로 찾아 인덱스에 위치한 문자열 출력.

word = input().upper()
word_list = list(set(word))
cnt = []

for i in word_list:
    count = word.count
    cnt.append(count(i))

    if cnt.count(max(cnt)) > 1:
        print('?')
    else:
        print(word_list[(cnt.index(max(cnt)))])

