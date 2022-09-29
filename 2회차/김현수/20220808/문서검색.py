import sys
sys.stdin = open("문서검색.txt")

#문서에서 특정 단어가 몇번 등장하는지 세는 문제

N = input() #전체 단어 
M = input() #str타입을 이용한 문제풀이
cnt = 0
#print(N)
while True:
    if M in N:
        N = N.replace(M,' ',1)
        cnt += 1
        #print(N)
    elif M not in N:
        print(cnt)
        break    
