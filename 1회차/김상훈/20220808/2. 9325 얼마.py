import sys
sys.stdin = open("2. 얼마.txt", "r")

T = int(input())
for _ in range(T):
    car = int(input()) # 차 가격
    C = int(input()) # 옵션 갯수
    
    result = car # 옵션 없이 차만 산 가격을 result에 저장
    
    for _ in range(C): #옵션 갯수만큼 입력받음(반복)
        x,y = map(int,input().split()) # 옵션 갯수와 가격
        result += x * y #  차의 가격 + 옵션 갯수* 옵션 가격
        
    print(result)
    