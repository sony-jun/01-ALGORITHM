
n = int(input())
nums = list(map(int,(input().split())))

temp = nums[0]
result = 0
answer = []

for i in range(1,n): # 리스트 인덱스 1번부터 검사
    if nums[i] > temp >0 : #더 큰 수가 나오면 그 차를 result에 더하기 
        result += nums[i]-temp
        temp = nums[i]
        
    elif nums[i] == temp or nums[i]-temp<0 : #같거나 작은 수가 나오면 오르막 끝내기
        answer.append(result)
        temp = nums[i] # 현재 수부터 오르막 새로 시작
        result = 0 
        
answer.append(result)

print(0 if len(answer)==0 else max(answer)) 