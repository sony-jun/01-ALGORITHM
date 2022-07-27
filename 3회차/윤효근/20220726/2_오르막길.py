import sys

sys.stdin = open("2_오르막길.txt")

a = int(input()) #5
b =list(map(int,input().split())) # 1 2 1 4 6
start = 0   #오르막길의 기울기 저장하는 변수
result=[]   #각각의 기울기를 저장
for i in range(a-1):
    if b[i] <b[i+1]:
        start += b[i+1] - b[i]
        #start에 b[i-1] - b[i] 값을 저장 => 각각의 값을 모두 더하면 최종 기울기가 나옴
    else:
        result.append(start) #result에 각 오르막길의 최종 기울기 저장
        start = 0       #start를 초기화하고 다음 오르막길 받을 준비
result.append(start)    #오르막길이 마지막에 있을 경우에도 저장

print(max(result))      #오르막길의 최대값 출력 => 가장 큰 오르막길 출력