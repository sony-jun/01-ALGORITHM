T = int(input())

for i in range(1,T+1): # for 반복문으로 레인지 함수를 사용사하여 a, b 합을 출력하기로 함
    a,b = map(int, input().split()) # a, b 는 맵 함수로 빈칸을 기준으로 입력받음
    print("Case #"+str(i)+':',a+b) # ':'과 a+b의 합이 떨어져있으므로 콤마(.)를 사용해 띄어서 출력하도록 했다
                                   # 케이스 넘버 i는 정수형이지만 문자형과 같이 붙여서 쓰기위해 같은 자료형인 str(i)로 바꿨다.