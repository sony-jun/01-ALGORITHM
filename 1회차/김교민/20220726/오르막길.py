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

# 예시

# n = int(input()) #반복할 횟수
# arr = list(map(int,input().split())) #리스트로 값을 입력받음
# start,end = arr[0],arr[0] 
# answ = 0
# for i in range(1,n):
#     if end >= arr[i]: #뒤에 수가 앞에 수보다 작은 경우 start, end를 뒤에 수로 설정
#         start = arr[i]
#         end = arr[i]
#     else:
#         end = arr[i] #뒤에 수가 앞에 수보다 큰경우 end를 뒤에 수로 설정
#     answ = max(answ,end-start)  #차이값이 큰 수를 answ에 넣는다
# print(answ)