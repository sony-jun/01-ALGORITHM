word = input().upper()
# 대소문자 구별 하지않고 낱말을 확인하고 대문자로 출력 할 것이기때문에 upper로 전부
# 대문자로 바꾸어 준다.
word_cha = list(set(word))
# word가 어떤 낱말들로 이루어 져 있는지 확인하기위해 set함수로 중복값을 제거하고 
# list로 순회 가능하도록 변경해줌

cha_num = []
# word_cha를 순회하며 각 낱말들이 몇개인지 확인하고 값을 입력해줄 빈 리스트 생성
for cha_ in word_cha:
    cha_num.append(word.count(cha_))
    # 생성해둔 cha_num에 word_cha에 있는 각 낱말들 최초 주어진 값을 upper해준 값에서
    # 몇 개씩 가지고 있는지 카운트하고 그 값을 append함수를 통해 넣어줌.
max_n = max(cha_num)
# cha_num에서 가장 큰 값이 무엇인지 찾아줌.

if cha_num.count(max_n) == 1:
    print(word_cha[cha_num.index(max_n)])
    # cha_num에서 가장 많이 나오는 낱말이 1개이면
    # cha_num에서 max_n이 위치하는 자리를 찾고
    # word_cha의 해당 자리에 위치한 값을 출력하고
else:
    print('?')
    # 이외의 경우 가장 많이 사용된 낱말이 여러개라는 뜻이므로 '?'를 출력함