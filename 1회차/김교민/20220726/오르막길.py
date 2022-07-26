n=int(input())
up = list(map(int, input().split()))
tmp = 0 #오르막길의 높이를 저장할 임시 변수
l = [] #높이를 집어넣을 리스트

for i in range(1, n): #1부터 n-1까지의 숫자들
    if up[i]>up[i-1]: #길의 끝부분이 첫부분보다 숫자가 클 경우
        tmp+=up[i]-up[i-1] # 끝부분에 첫부분을 빼고 tmp에 넣음
        if i==n-1: #만약 i가 n-1이고 오르막길인 경우를 생각해서 if 문을 활용
            l.append(tmp)
    else: #오르막길이 아닌경우
        l.append(tmp)
        tmp=0 #tmp를 0으로 초기화
print(max(l))