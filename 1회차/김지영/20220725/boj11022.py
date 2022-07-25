T = int(input())
r = []
# 결과를 test_case돌때마다 출력하는게 아니라 한번에 출력 해야하네요.
# 빈 리스트를 만들고 result를 집어넣어 리스트가 다 완성된 후 출력해줍시다.
# 입력값의 seperator는 split함수 안에 넣기
# 테스트케이스마다 받은 값을 추적하려면 추적하려는 값마다 변수를 지정해준 후, 변수값마다 모아야하니 리스트를 만들어줘야할텐데 너무 번거로울거같아요.
# 방법은 모르겠으니까 제가 할 수 있는 방법을 사용하겠습니다.
# 출력 문장 자체를 리스트에 집어넣어버릴게요.
# 나중에 다른분 코드 보고 더 깔끔하게 만들 수 있도록 공부하겠습니다.
for test_case in range(T):
    A, B = map(int, input().split())
    C = A + B
    result = 'Case #'+str(test_case+1)+': '+ str(A)+' + '+str(B)+' = '+str(C)
    r.append(str(result))
# 리스트 출력
for test_case in r:
    print(test_case)