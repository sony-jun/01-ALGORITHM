# https://www.acmicpc.net/problem/2577
import sys
from telnetlib import PRAGMA_HEARTBEAT

sys.stdin = open("0_숫자의개수.txt")
#A*B*c 결과 
# 0~9까지 확인
#그 결과 출력
A=int(input())
B=int(input())
C=int(input())
OP=[0,0,0,0,0,0,0,0,0,0]
result=A*B*C
result=list(map(int, str(result)))#리스트로 변환
result.sort()#정렬하고 
for i in result:
    if i == 0:
        OP[0]+=1
    elif i == 1:
       OP[1]+=1
    elif i == 2:
       OP[2]+=1
    elif i == 3:
       OP[3]+=1
    elif i == 4:
       OP[4]+=1
    elif i == 5:
       OP[5]+=1
    elif i == 6:
       OP[6]+=1
    elif i == 7:
       OP[7]+=1
    elif i == 8:
       OP[8]+=1
    elif i == 9:
       OP[9]+=1
    else:
     OP= OP
for k in OP:
    print(k)
