N = int(input())

for number in range(1, N + 1): # 1부터 N까지의 모든 수의 분해합을 탐색
    split_sum = 0 # 분해합을 저장할 변수

    for digit in str(number): # 각 자리수를 문자열로 변환하고
        split_sum = split_sum + int(digit) # 각자리수의 합을 split_sum에 저장시켜줌
    split_sum = split_sum + number # 각 자리의 합과 number를 더하면 분해합의 조건에 충족됨
    
    if split_sum == N: # 만약 split_sum이 입력한 값과 같다면 출력 후 브레이크
        print(number)
        break
else: # for-else를 이용해 아니면 0을 출력
    print('0')