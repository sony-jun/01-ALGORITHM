# 빨간 숫자로 표시된 나머지 변의 길이를 출력하면 된다.

T = int(input())
for i in range(1,T+1):
    a, b, c= map(int,input().split())
    if a==b:
        print("#%d %d" %(i,c))
    else:
        print("#%d %d" %(i,a))