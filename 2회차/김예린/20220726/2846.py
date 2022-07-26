# 오르막길

n = int(input())                       # 입력값은 5로 가정
nums = list(map(int, input().split())) # 입력값을 리스트 형태로 담아준다. 
cnt = 0                                # 빼준 값을 저장
result = []                            # 오르막길 값을 저장

for i in range(n - 1):                 # if 문에 [i+1]로 다음 값과 비교하기 때문에 n에서 1을 빼줘야 한다. 
                                       # n을 넣는다면 [i+1]에서 범위에 있는 값이 없기 때문에 오류가 난다. 

    if nums[i] < nums[i + 1]:          # 만약 다음 인덱스 값이 크다면
        cnt += (nums[i + 1] - nums[i]) # 빼줘서 cnt에 값을 넣는다. 

    if nums[i] >= nums[i + 1]:         # 만약 다음 인덱스가 같거나 작다면 (오르막길이 아닐 경우)
        result.append(cnt)             # 위 cnt값(인덱스를 빼준 값)을 result에 넣어주고 
        cnt = 0                        # cnt는 0으로 초기화한다. 
                                       # 두 번째 if문에서 cnt(빼준)값을 result에 넣는 이유는 더 큰 오르막길이 있을 경우를 위함

result.append(cnt)                     # for문을 반복하여 오르막길 값을 구한뒤 for문이 종료되고 마지막으로 계산한 값을 result에 넣어준다. 

print(max(result))                     # result에 저장된 큰 수를 출력한다. 

# 숫자가 커질 때 더하고 작아질 때 0으로 초기화한다.
