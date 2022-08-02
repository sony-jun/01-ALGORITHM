import sys
sys.stdin = open('인사성밝은곰곰이_input.txt')

# 하나씩 빼고 enter면 그냥 아무것도 안하고 리스트에 담아서

T = int(input())
enter = str(input()) #ENTER을 입력받고 시작
cnt= 0 #곰곰티콘 사용횟수
gom = {}

for i in range(1,T):
    name = str(input()) #입장한 사람
    if name =="ENTER": #Enter가 입력되면
        for k, v in gom.items():
            if v ==1:  
                cnt+=1 
        gom={} 
        continue
    if name not in gom:
        gom[name] = 1 

for k,v in gom.items():
    if v==1:
        cnt+=1

print(cnt)     