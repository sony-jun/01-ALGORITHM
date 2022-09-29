# https://www.acmicpc.net/problem/5622

#시간 1->2초, 2>3초, 3>4초...9>10초 ,0>11초
#if문으로 숫자+1초, 

list_= ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

s = input()
re = 0

for i in s :
    for j in list_:
        if i in j:
            re += list_.index(j) + 3
print(re)



            
