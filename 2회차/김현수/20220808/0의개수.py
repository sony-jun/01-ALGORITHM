import sys
sys.stdin = open("0의개수.txt") #count('0')이용하기 

T = int(input())
for _ in range(T):
    cnt = 0
    N, M = map(int,(input().split()))
    for i in range(N,M+1):
        list_str = str(i)
        for j in list_str:
            if j == '0' :
                cnt +=1
    print(cnt)