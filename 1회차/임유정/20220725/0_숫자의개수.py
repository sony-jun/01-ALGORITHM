# # https://www.acmicpc.net/problem/2577
# import sys
# sys.stdin = open("0_숫자의개수.txt")

num=[] #먼저, 리스트 값을 선언해줌. 아래에서 곱셈한 값에서 숫자 한자리씩 추가할때 사용할 리스트
A=int(input())
B=int(input())
C=int(input())
T=str(A*B*C) #아래와 같이 나온 값들을 숫자 한자리씩 슬라이싱을 해주기 위하여 문자열로 변환시켜야함.
for i in T: 
    num.append(i) # T변수에 저장되어 잇는 문자열을 슬라이싱하여 한자리씩 num이라는 리스트에 추가
                  # 자리수를 하나씩 쪼개고 다음열로 구성하는 단계로 이해 1234567 [1,2,3,4,5,6,7]

for i in range(10) :     #0부터 9까지의 숫자가 각각 몇 번 쓰였는지 확인을 하기 위해 반복문의 횟수를 10번으로 설정
    print(num.count(str(i)))  #count함수를 이용해 문자열로 num 값이쪼개진 글자 하나값 str(i)값을 세어준다 
      
