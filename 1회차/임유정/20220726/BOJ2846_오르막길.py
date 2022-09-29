N = input()
slope = input().split()
slope_sum = 0
slope_num = [0] ## 내리막일 경우 하나도 쌓이지 않는다.
#print(slope)

for i in range(0, int(N) - 1):
    ## int 만 있고 없고 차이로 왜지...
		## 비교 하려는 자리와 바로 다음자리 수를 비교해서 오르막이라면
    if int(slope[i]) < int(slope[i+1]):
        #print(int(slope[i+1]) - int(slope[i]))
				## 슬로프썸에 차이만큼 누적하여 더한다.
        slope_sum += int(slope[i+1]) - int(slope[i])
				## 누적한 수를 append한다
        slope_num.append(slope_sum)
    else:
				## 내리막이라면 썸을 0으로 바꿔
        slope_sum = 0
print(max(slope_num))