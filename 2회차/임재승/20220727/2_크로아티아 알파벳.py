# https://www.acmicpc.net/problem/2941

T = input()


# c=, c-, d-, lj, nj, s=, z= 두 스펠링이 한 스펠링이고
# dz= 세 스펠링이 한 스펠링
# len 에서 저만큼 빼준다.
# 다만 dz=은 z=이랑 중복이라서 한개만 빼주면 된다.
def cro(n):
    min_len = 0
    min_len += n.count('c=')
    min_len += n.count('c-')
    min_len += n.count('d-')
    min_len += n.count('lj')
    min_len += n.count('nj')
    min_len += n.count('s=')
    min_len += n.count('z=')
    min_len += n.count('dz=')
    answer = len(n) - min_len
    return answer

print(cro(T))



# HR_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# t = input()

# for i in HR_alphabet:
#     t = t.replace(i, '*')

# print(len(t))