# 백준 2941번
# ljes=njak는 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어짐
# 단어가 주어졌을 때 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력

# dž는 무조건 하나의 알파벳. 서로 분리된 것으로 보지 않음.
# lj와 nj도 마찬가지. 위 목록에 없는 알파벳은 한 글자씩 센다

# 첫째 줄에 최대 100글자의 단어가 주어진다
# 알파벳 소문자와 '-', '=' 로만 이루어짐

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia:
    # 문자를 변환하는 함수 replace 사용
    # replace는 사용한 문자열 원형을 변형시키지 않음
    word = word.replace(i, '*')
print(len(word))