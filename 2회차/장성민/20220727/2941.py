# 크로아티아 리스트 생성
cro_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# 문자열 입력
word = input()

# 반복/조건을 통해 크로아티아 문자 찾으면 변경("0")
for i in cro_list:
    if i in word:
        word = word.replace(i, "0")

# 총 글자수 출력
print(len(word))

