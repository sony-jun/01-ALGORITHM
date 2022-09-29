# 2941. 크로아티아 알파벳
"""
ljes=njak은 
크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다.
단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
dž는 무조건 하나의 알파벳으로 쓰이고, 
d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다. 
위 목록에 없는 알파벳은 한 글자씩 센다.

# 입력
첫째 줄에 최대 100글자의 단어가 주어진다. 
알파벳 소문자와 '-', '='로만 이루어져 있다.
단어는 크로아티아 알파벳으로 이루어져 있다.
 문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.
 
 # 출력
 입력으로 주어진 단어가
 몇 개의 크로아티아 알파벳인지 출력한다.
 
 # 접근
 1. 변경된 크로아티아 알파벳의 두번재 글자는
 2. =, -, j 로 이루어져 있다.
 3. 문자열을 순회하다가 해당 글자를 만나면,
 4. =, -는 등장하기만 하면 카운트하면 되지만,
 5. j로 끝나는 알파벳은 알파벳이거나 크로아티아 알파벳이므로
 6. 직전 인덱스로 접근하여 비교한다.
 7. 누적된 카운트와
 
"""
word = input()
kro = 0
kro_l = []
for i in word:
    if i == '=':
        kro += 1
        new_word = word.replace('c=', "")
        new_word = word.replace('dz=', "")
        new_word = word.replace('s=', "")
        new_word = word.replace('z=', "")
    if i == '-':
        kro += 1
        new_word = word.replace('c-', "")
        new_word = word.replace('d-', "")
for idx in range(1, len(word)):
    if word[idx] == 'j':
        if word[idx - 1] == 'n':
            new_word = word.replace('nj',"")
        if word[idx - 1] == 'l':
            new_word = word.replace('lj',"")
print(kro_l)
print(new_word)
            
            