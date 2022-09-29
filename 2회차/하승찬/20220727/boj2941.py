#크로아티아 알파벳

n = input()

char=[]

for i in range(len(n)): # 길이로 하나씩 비교하자.
    if n[i] =='-':
        if n[i-1:i]== 'c':
            char.remove('c')
            char.append('-c')
        elif n[i-1:i]=='d':
            char.remove('d')
            char.append('-d')
    elif n[i] =='=':
        if n[i-1:i]== 'c':
            char.remove('c')
            char.append('=c')
        elif n[i-1:i]=='s':
            char.remove('s')
            char.append('=s')
        elif n[i-1:i]=='z':
            if n[i-2:i-1]=='d':
                char.remove('z')
                char.remove('d')
                char.append('=zd')
            else:
                char.remove('z')
                char.append('=z')

    elif n[i] == 'j': 
        if n[i-1:i]== 'n':
            char.remove('n')
            char.append('nj')
        elif n[i-1:i]=='l':
            char.remove('l')
            char.append('lj')#만약 j로 먼저시작한다면??
        else:
            char.append(n[i])

    else:
        char.append(n[i])

print(len(char))
# #	c=
# ć	c-
# dž	dz=
# đ	d-
# lj	lj
# nj	nj
# š	s=
# ž	z=