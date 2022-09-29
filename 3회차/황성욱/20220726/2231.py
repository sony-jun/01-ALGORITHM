n = int(input())
is_in = False  # 범위 안에서 생성자가 있는지 체크하기 위해서
for i in range(1, n): # 생성자는 n보다 클 수 없기 때문에 n까지 범위를 설정
    sum_val = 0 # 각 자리수의 합을 구하기 위해 변수 생성
    for j in str(i): # str 로 변환하여 각 자리수 순회하며 sum_val에 더해줌
        sum_val += int(j)
    if sum_val + i == n: # 1 ~ n 중 i 의 분해합과 각 자리수의 합이 n과 같으면 for문을 탈출
        print(i)
        is_in = True
        break
if is_in == False: # 생성자가 없어 is_in 이 False 일 때, 0을 출력
    print(0)




