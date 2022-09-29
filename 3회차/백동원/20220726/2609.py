A, B = map(int, input().split())

for i in range(A, 0, -1):                   # 입력한 두 수 중 아무 숫자부터 1까지 역으로 순회한다.
    if A % i == 0 and B % i == 0:           # 만약 두 수를 나눴을 때 나머지가 0인 수를 찾았다면 그 수는 최대공약수이다.
       print(i)                             # 최대공약수를 출력하고
       print(int(i * (A / i) * (B / i)))    # 최소공배수는 두 수를 최대공약수로 나눈 것을 곱한 값에 최대공약수를 곱한 값이다.
       break                                # 반복하지 않게 break
