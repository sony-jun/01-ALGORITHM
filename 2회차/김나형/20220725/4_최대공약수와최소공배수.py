import sys

sys.stdin = open("4_최대공약수와최소공배수.txt")


a, b  = map(int, input().split()) # 24 18
for i in range(min(a,b),0,-1): # 19~24는 18의 공약수가 될 수 없음으로 두 정수중 작은 값으로 하나하나 비교해 줌.
    if a % i  == 0 and b % i == 0: # 공약수는 두 값의 몫이 0 이어야 한다.     
        print(i,(a*b//i),sep='\n')
        # 최대공배수는 두 값 곱을 약수로 나눈 값과 동일
        break


