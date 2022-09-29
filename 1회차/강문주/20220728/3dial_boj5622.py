dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
sec = 0
for i in range(len(a)):
    for j in dial:
        if a[i] in j:
            sec += dial.index(j)+3 #a값과 일치하는 리스트에 인덱스를 반환 그리고 최소시간 ABC는 2번이고 인덱스가 0이기 떄문에 3을 더함 
print(sec)
