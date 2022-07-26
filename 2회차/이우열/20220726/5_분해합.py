n = int(input())

for i in range(n):
    arr = list(map(int, str(i)))        # 숫자를 쪼개서 배열에 저장
    temp = i + sum(arr)                 # 숫자와 배열의 합의 합을 계산

    if temp == n:                       # 입력받은 수와 temp가 같다면 생성자 만족
        result = i                      # i가 생성자가 됨
        print(result)
        break
else:
    print('0')                          # 생성자가 없다면 0 출력
