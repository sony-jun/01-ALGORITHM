# https://www.acmicpc.net/problem/2577
a , b , c = map(int, input().split()) # a b c의 인풋을 받아오는 코드
y = a * b * c # a b c를 곱한것은 y
x = [0] * 10 #리스트 자료형 [0 을 10개 생성]
while y != 0: #a b c를 곱한 값이 0이 아니면 트루(0될떄까지 식을 계속)
    x[y % 10] += 1 
    y //= 10
#for i in x:
#    print(i) 