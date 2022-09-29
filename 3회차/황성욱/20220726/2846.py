n = int(input()) # 배열의 갯수 입력
n_list = list(map(int, input().split())) # 입력 받은 배열을 리스트로 저장
sum_val = 0 
res = [] # 배열의 뺀 값을 저장하기 위해 빈 리스트 생성
for i in range(len(n_list)-1): # 배열의 i번째항이 i+1번째 항보다 작으면 두 항의 차를 sum_val에 더해줌
    if n_list[i] < n_list[i + 1]:
        sum_val += (n_list[i + 1] - n_list[i])
    else: # if 문의 조건을 만족하지 않으면 sum_val을 0으로 초기화
        
        sum_val = 0
    res.append(sum_val)
    print(res)

print(max(res)) # 뺀값의 리스트 중 최댓값이 최대의 오르막길 크기이기 때문에

