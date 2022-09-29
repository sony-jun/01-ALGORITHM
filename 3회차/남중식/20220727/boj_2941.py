# 입력된 문자는 몇 개의 크로아티아 알파벳으로 변환되는가

T = input()

c_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for c in c_list:
    T = T.replace(c, 'x')
    
print(len(T))