# https://www.acmicpc.net/problem/2577
import sys

#방법1
sys.stdin = open("0_숫자의개수.txt")

a = int(input())
b = int(input())
c = int(input())
total = str(a*b*c)

for num in range(10): #for문을 이용해서 0~9까지 숫자 범위 생성
    num_count = total.count(str(num)) #0~9까지 숫자가 몇번 쓰였는지 알기 위해 count함수 사용하였고 
    #17037300라는 문자열에서 카운트함수 사용하여 각 자릿수('0','1' 등)의 문자열 갯수체크
    #예:  'ooyyy'.count('y') > 3
    # 해당 함수 괄호 안에는 찾는 문자열을 입력해야 하기 때문에 0~9를 문자열로 변환
    print(num_count)

#방법2
total1 = 1
for i in range(3): # for문 3번반복
    n = int(input()) # 3번입력 받음
    total1 *= n # 입력 받은 3개 수를 곱하여 total1변수에 할당  
total_str = str(total1) #각 자릿수를 분리하기 위해 문자열로 전환

for num in range(10): #숫자 범위 생성, 10번반복
    num_count = total_str.count(str(num))#반복한것을 숫자로 변환, Count함수는 위 참고 
    print(num_count)
