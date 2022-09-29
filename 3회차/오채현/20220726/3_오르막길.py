from turtle import up


n = int(input())
h = list(map(int, input().split()))
uphill = 0
result = []

for i in range(n-1):
    #측정한 높이 값 리스트에서 인덱스로 앞뒤 값 비교해서 오르막인지 확인
    if h[i] < h[i + 1]: 
        #오르막이면 높이 차 구해서 uphill에 대입  계속 오르막이면 값 누적
        uphill += h[i + 1] - h[i]
    if h[i] >= h[i + 1]:
        #오르막 아니면 앞에 누적된 값 result로 넘겨두고 uphill다시 초기화 뒤에 오르막 있는지 확인
        result.append(uphill)
        uphill = 0
result.append(uphill)
#result에 저장된 누적된 값들 중 큰 값이 가장 큰 오르막길
print(0) if len(result) == 0 else print(max(result))