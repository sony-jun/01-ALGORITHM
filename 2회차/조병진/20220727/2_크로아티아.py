# 크로아티아 알파벳
# 문제 : 해당 크로아티아 문자로 변환하고, 변환한 문자열의 글자수를 출력

word = input()

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia:
    word = word.replace(i, '*')

print(len(word))
