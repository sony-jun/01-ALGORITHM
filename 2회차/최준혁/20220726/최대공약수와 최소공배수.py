A, B = map(int, input().split())
# 최대공약수? 두 수에 대해 나눠지는 수 중에 제일 높은 수
# 최소 공배수 두 수를 곱할 때 같아지는 수 중 최소 수
# 유클리드 호제법으로 최대공약수 구하기
result = []

def GCD(x, y):
    while(y): # y가 0이 될때까지 
        # x = 24, y = 18, r = x%y 

        # 24 % 18 = 6
        # 18 % 6 = 0 
        x, y = y, x%y # x, y의 최대 공약수는 y와 x%y의 최대공약수와 같다
        min = A*B/x
    print(x)
    print(int(min))
    
GCD(A, B)

