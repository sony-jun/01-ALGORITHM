T = int(input())

for i in range(1,T+1): #t만큼 for반복문의 레인지 함수를 활용해 반복한다.
    a,b = map(int, input().split()) # 그리고 조건에 맞게 a, b 의 입력값을 map 합수로 묶어 빈칸을 기준으로 a,b 구별해 int 자료형으로 바꾸어줌
    0 < a and  10>b # 조건에 맞게 a, b 의 범위를 설정하고 c를 a+b의 합의 변수로 만들었음.
    c=a+b
    
    print('Case #'+str(i)+':',str(a),'+',str(b),'=',c)
    # 같은 자료형끼리만 가능하기 때문에 정수형 i, a, b를 str(문자형)로 바꾸어 사용하였다.