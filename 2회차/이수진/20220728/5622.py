# a=input()
# sec=0
# for i in a:
#     if ord(i) in range(65,68):
#         sec+=3
#     if ord(i) in range(68,71):
#         sec+=4
#     if ord(i) in range(71,74):
#         sec+=5
#     if ord(i) in range(74,77):
#         sec+=6
#     elif ord(i) in range(77,80):
#         sec+=7
#     elif ord(i) in range(80,84):
#         sec+=8
#     elif ord(i) in range(84,87):
#         sec+=9
#     elif ord(i) in range(87,91):
#         sec+=10
# print(sec)


granma=input()
dial=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
sec=0
for i in dial:
    for j in granma:
        if j in i :
            sec+=dial.index(i)+3
print(sec)