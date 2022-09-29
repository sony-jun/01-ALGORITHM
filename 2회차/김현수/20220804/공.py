import sys
sys.stdin = open('공.txt','r')

cup = [1, 0, 0]
M = int(input())
for _ in range(M):
    a, b = map(int,input().split())
    cup[a-1], cup[b-1] = cup[b-1], cup[a-1]
    #print(cup)
for _ in range(3):
    if cup[_] == 1 :
        ansmwer = _ + 1 #인덱스값과 현실숫자 차이 생각할것

print(ansmwer)