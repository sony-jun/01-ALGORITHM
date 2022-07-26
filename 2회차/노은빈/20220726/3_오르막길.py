n = int(input())  #측정한 높이의 수이자 수열의 크기
l = list(map(int,input().split()))  #n개의 양의 정수

cnt = 0
h = [] #오르막길 길이

for i in range (len(l) - 1):  #0~4
    if l[i] < l[i+1] :  #i값이 i+1보다 작다면
        cnt += l[i+1] - l[i]  #i+1값 - i값을 cnt에 더함(오르막길임)

    if l[i] >= l[i+1] : #i값이 i+1보다 크다면
        cnt = 0       #오르막길 아님 => 만약 오르막길이 없다면 0출력
        h.append(cnt)    
    h.append(cnt)

print(max(h))   #i+1값 - i값 중 가장 큰 값 출력

