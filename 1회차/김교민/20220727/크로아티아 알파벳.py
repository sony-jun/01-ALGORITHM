# 변경된 크로아티아 알파벳을 넣어두기
croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
str_ = input()

for i in croa:
#input시킨 str_에 croa안의 크로아티아 알파벳을 찾아서 *로 바꿔주기
    str_ = str_.replace(i, '*')
print(len(str_))#str_길이를 출력한다.