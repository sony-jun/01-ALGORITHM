# 킹과 돌의 마지막 위치를 구하는 프로그램을 작성하시오.

import sys
sys.stdin = open("1063.txt")


# 좌표 움직임을 저장한 딕셔너리
move = {
    "R":[1,0],
    "L":[-1,0],
    "B":[0,-1],
    "T":[0,1],
    "RT":[1,1],
    "LT":[-1,1],
    "RB":[1,-1],
    "LB":[-1,-1]
}

# 리스트 간 덧셈
def list_sum(a,b):
    return [a[0]+b[0],a[1]+b[1]]

k, s, N = input().split()
N = int(N)
# 킹과 돌의 위치 표현 : 숫자로 변환해서 표현
k = list(k)
s = list(s)
k=[ord(k[0])-64,int(k[1])]
s=[ord(s[0])-64,int(s[1])]

for i in range(N):
    m = input()
    if 1<=k[0]<=8 and 1<=k[1]<=8 and 1<=s[0]<=8 and 1<=s[1]<=8: # 문제발생
        k=list_sum(k,move[m])
        s=list_sum(s,move[m])
    else:
        continue

k=[chr(k[0]+64),str(k[1])]
s=[chr(s[0]+64),str(s[1])]
k="".join(k)
s="".join(s)
print(k,s)
