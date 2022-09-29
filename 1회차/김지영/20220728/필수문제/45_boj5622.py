# 숫자를 문자로..기억하시는 할머니
# [1,'ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ','OPQRST',0]
# 1을 핀까지 돌리는데 2초, 2는 3초,3은 4초...n+2초?
dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
time = 0
word = input()

for i in word:
    for j in dial:  # word에서 dial 요소 찾아
        if i in j:
            # print(i,j,'num=',dial.index(j)+1,'time=',dial.index(j)+2)
            time += dial.index(j)+3
print(time)