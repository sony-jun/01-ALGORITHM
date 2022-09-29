# 백준 1157
# 알파벳 대소문자로 된 단어가 주어지면
# 이 단어에서 가장 많이 사용된 알파벳이 무엇인지?
# 대소문자 구별하지 않음

# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력
# 가장 많이 사용된 알파벳이 여러개 존재하는 경우 ? 출력

# 입력 받은 문자를 전부 대문자로 바꿔줌
word = input().upper()
# 리스트화하여 중복값 제거
word_list = list(set(word))
cnt = []

for i in word_list:
    count = word.count
    # 알파벳이 사용된 횟수를 리스트에 저장
    cnt.append(count(i))

# count 숫자 최대값이 중복되면 ? 출력
if cnt.count(max(cnt)) > 1:
    print('?')
# count 숫자 최대값 인덱스(위치)
else:
    print(word_list[(cnt.index(max(cnt)))])